# One-off script version 2
import sys
import subprocess

from dp_tools.glds_api.commons import *

if len(sys.argv) != 4:
    print("Error improper usage:")
    print("Usage: 'python get_file_urls.py <OSD-ACCESSION> <REGEX-FILE-PATTERN> <output_dir>'")
    print("  E.g: 'python get_file_urls.py OSD-194 genes.results outputDir'")
    sys.exit(1)

print(f"Fetching for within '{sys.argv[1]}'")
print(f"Pattern: {sys.argv[2]}")

fns = find_matching_filenames(accession = sys.argv[1], filename_pattern = sys.argv[2])

if len(fns) == 0:
    print(f"No files found matching the pattern: '{sys.argv[2]}'")
    input(f"Press enter to print all files found and exit program: ")
    for associated_file in get_table_of_files(sys.argv[1])['file_name']:
        print(associated_file)

for fn in fns:
    url = retrieve_file_url(accession = sys.argv[1], filename = fn)
    command = f"curl {url} -L --create-dirs  -o {sys.argv[3]}/{fn}"
    print(f"running: {command.split()}")
    subprocess.run(command.split())