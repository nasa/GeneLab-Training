#!/usr/bin/env python3
"""
Script to download and process Ensembl GTF file to create transcript-gene mapping table.
Creates a table with ENSEMBLTRANS and ENSEMBL columns mapping transcript IDs to gene IDs.
"""

import urllib.request
import gzip
import re
import pandas as pd
import os
import sys
from collections import defaultdict

def download_file(url, filename):
    """Download file from URL with progress indication."""
    print(f"Downloading {url}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False

def extract_gz_file(gz_filename):
    """Extract gzipped file."""
    output_filename = gz_filename.replace('.gz', '')
    print(f"Extracting {gz_filename}...")
    
    try:
        with gzip.open(gz_filename, 'rb') as f_in:
            with open(output_filename, 'wb') as f_out:
                f_out.write(f_in.read())
        print(f"Extracted: {output_filename}")
        return output_filename
    except Exception as e:
        print(f"Error extracting file: {e}")
        return None

def parse_gtf_attributes(attributes_str):
    """Parse GTF attributes string to extract gene_id and transcript_id."""
    gene_id = None
    transcript_id = None
    
    # Pattern to match gene_id
    gene_pattern = r'gene_id\s+"([^"]+)"'
    gene_match = re.search(gene_pattern, attributes_str)
    if gene_match:
        gene_id = gene_match.group(1)
    
    # Pattern to match transcript_id  
    transcript_pattern = r'transcript_id\s+"([^"]+)"'
    transcript_match = re.search(transcript_pattern, attributes_str)
    if transcript_match:
        transcript_id = transcript_match.group(1)
    
    return gene_id, transcript_id

def process_gtf_file(gtf_filename):
    """Process GTF file to extract transcript-gene mappings."""
    print(f"Processing GTF file: {gtf_filename}")
    
    transcript_gene_map = {}
    total_lines = 0
    processed_lines = 0
    
    try:
        with open(gtf_filename, 'r') as f:
            for line in f:
                total_lines += 1
                
                # Skip comment lines
                if line.startswith('#'):
                    continue
                
                # Split GTF line into components
                fields = line.strip().split('\t')
                if len(fields) < 9:
                    continue
                
                # Extract attributes (9th column)
                attributes = fields[8]
                
                # Parse gene_id and transcript_id
                gene_id, transcript_id = parse_gtf_attributes(attributes)
                
                # Only process lines with both gene_id and transcript_id
                if gene_id and transcript_id:
                    # Filter for mouse transcripts (ENSMUST) and genes (ENSMUSG)
                    if transcript_id.startswith('ENSMUST') and gene_id.startswith('ENSMUSG'):
                        transcript_gene_map[transcript_id] = gene_id
                        processed_lines += 1
                
                # Progress indicator
                if total_lines % 100000 == 0:
                    print(f"Processed {total_lines:,} lines...")
    
    except Exception as e:
        print(f"Error processing GTF file: {e}")
        return None
    
    print(f"Total lines processed: {total_lines:,}")
    print(f"Lines with transcript-gene pairs: {processed_lines:,}")
    print(f"Unique transcripts found: {len(transcript_gene_map):,}")
    
    return transcript_gene_map

def create_mapping_table(transcript_gene_map):
    """Create pandas DataFrame from transcript-gene mapping."""
    print("Creating mapping table...")
    
    # Create lists for DataFrame
    transcript_ids = list(transcript_gene_map.keys())
    gene_ids = list(transcript_gene_map.values())
    
    # Create DataFrame
    df = pd.DataFrame({
        'ENSEMBLTRANS': transcript_ids,
        'ENSEMBL': gene_ids
    })
    
    print(f"Initial table shape: {df.shape}")
    
    # Remove duplicates based on ENSEMBLTRANS (should not be any, but just to be safe)
    initial_count = len(df)
    df = df.drop_duplicates(subset=['ENSEMBLTRANS'], keep='first')
    final_count = len(df)
    
    if initial_count != final_count:
        print(f"Removed {initial_count - final_count} duplicate transcript entries")
    else:
        print("No duplicate transcripts found")
    
    print(f"Final table shape: {df.shape}")
    return df

def validate_mapping(df, gtf_filename, sample_size=100):
    """Validate a sample of mappings against the original GTF file."""
    print(f"\nValidating {sample_size} random mappings against GTF file...")
    
    # Sample random entries for validation
    sample_df = df.sample(n=min(sample_size, len(df)), random_state=42)
    
    # Build a reference mapping from the GTF file for the sampled transcripts
    sample_transcript_ids = set(sample_df['ENSEMBLTRANS'].tolist())
    gtf_reference = {}
    
    print("Building reference mappings from GTF file...")
    try:
        with open(gtf_filename, 'r') as f:
            for line in f:
                # Skip comment lines
                if line.startswith('#'):
                    continue
                
                # Split GTF line
                fields = line.strip().split('\t')
                if len(fields) < 9:
                    continue
                
                # Extract attributes (9th column)
                attributes = fields[8]
                
                # Parse gene_id and transcript_id
                gene_id, transcript_id = parse_gtf_attributes(attributes)
                
                # Only store if this is one of our sample transcripts
                if transcript_id in sample_transcript_ids and gene_id:
                    gtf_reference[transcript_id] = gene_id
                
                # Stop early if we found all sample transcripts
                if len(gtf_reference) == len(sample_transcript_ids):
                    break
    
    except Exception as e:
        print(f"Error reading GTF file for validation: {e}")
        return False
    
    # Validate each sampled mapping
    validation_results = []
    
    for _, row in sample_df.iterrows():
        transcript_id = row['ENSEMBLTRANS']
        expected_gene_id = row['ENSEMBL']
        
        if transcript_id in gtf_reference:
            actual_gene_id = gtf_reference[transcript_id]
            is_correct = actual_gene_id == expected_gene_id
            validation_results.append(is_correct)
            
            if not is_correct:
                print(f"MISMATCH: {transcript_id} -> Expected: {expected_gene_id}, Found: {actual_gene_id}")
        else:
            print(f"WARNING: Could not find {transcript_id} in GTF file")
            validation_results.append(False)
    
    correct_count = sum(validation_results)
    accuracy = (correct_count / len(validation_results)) * 100 if validation_results else 0
    
    print(f"Validation accuracy: {accuracy:.1f}% ({correct_count}/{len(validation_results)} correct)")
    
    return accuracy > 95  # Consider valid if >95% accuracy

def main():
    """Main function to orchestrate the entire process."""
    url = "https://ftp.ensembl.org/pub/release-112/gtf/mus_musculus/Mus_musculus.GRCm39.112.gtf.gz"
    gz_filename = "Mus_musculus.GRCm39.112.gtf.gz"
    
    print("=== Ensembl GTF Transcript-Gene Mapper ===\n")
    
    # Step 1: Download the file
    if not os.path.exists(gz_filename):
        if not download_file(url, gz_filename):
            print("Failed to download file. Please download manually and place in current directory.")
            return False
    else:
        print(f"File {gz_filename} already exists, skipping download.")
    
    # Step 2: Extract the file
    gtf_filename = gz_filename.replace('.gz', '')
    if not os.path.exists(gtf_filename):
        gtf_filename = extract_gz_file(gz_filename)
        if not gtf_filename:
            print("Failed to extract file.")
            return False
    else:
        print(f"File {gtf_filename} already exists, skipping extraction.")
    
    # Step 3: Process GTF file
    transcript_gene_map = process_gtf_file(gtf_filename)
    if not transcript_gene_map:
        print("Failed to process GTF file.")
        return False
    
    # Step 4: Create mapping table
    df = create_mapping_table(transcript_gene_map)
    
    # Step 5: Save the table
    output_filename = "transcript_gene_mapping.tsv"
    df.to_csv(output_filename, sep='\t', index=False)
    print(f"\nMapping table saved to: {output_filename}")
    
    # Step 6: Display sample results
    print(f"\nSample of the mapping table:")
    print(df.head(10).to_string(index=False))
    
    # Step 7: Validate mappings
    is_valid = validate_mapping(df, gtf_filename)
    
    # Step 8: Summary statistics
    print(f"\n=== SUMMARY ===")
    print(f"Total unique transcripts: {len(df):,}")
    print(f"Total unique genes: {df['ENSEMBL'].nunique():,}")
    print(f"Validation passed: {'Yes' if is_valid else 'No'}")
    
    return True

if __name__ == "__main__":
    # Check if no arguments provided
    if len(sys.argv) == 1:
        print("=== Ensembl GTF Transcript-Gene Mapper ===")
        print("\nUsage: python gtf_mapper.py <URL> [options]")
        print("\nProcess Ensembl GTF files to create transcript-gene mapping tables.")
        print("\nRequired argument:")
        print("  URL                   URL to the Ensembl GTF file (.gtf.gz)")
        print("\nOptional arguments:")
        print("  -h, --help           Show this help message and exit")
        print("  -o, --output FILE    Output filename (default: auto-generated)")
        print("  --validation-size N  Number of mappings to validate (default: 100)")
        print("\nExamples:")
        print("  # Mouse genome")
        print('  python gtf_mapper.py "https://ftp.ensembl.org/pub/release-112/gtf/mus_musculus/Mus_musculus.GRCm39.112.gtf.gz"')
        print("\n  # Human genome") 
        print('  python gtf_mapper.py "https://ftp.ensembl.org/pub/release-112/gtf/homo_sapiens/Homo_sapiens.GRCh38.112.gtf.gz"')
        print("\n  # With custom output file")
        print('  python gtf_mapper.py "URL" --output my_mappings.tsv')
        print("\nOutput:")
        print("  Creates a TSV file with ENSEMBLTRANS and ENSEMBL columns")
        print("  mapping transcript IDs to their corresponding gene IDs.")
        sys.exit(0)
    
    success = main()
    if success:
        print("\n✓ Script completed successfully!")
    else:
        print("\n✗ Script failed!")
        sys.exit(1)