# Unix_Intro_JN_06-2021.ipynb Challange Question Answer Key:

---
### Section 1b.

**How many lines does the head command print by default?**
> 10

**What happened when you tried executing head -h?**
> We get an “invalid option” error

**Is -h a valid option for the head command? How do you know?** 
> No because it gave an error

---
## Section 2.

**What would you add to the head command to view the first 13 lines of the example.txt file?** 
> `-n 13`

---
### Section 2a.

**Where are you located within the SJSU cluster?** 
> /home/username

**Did you notice any familiar files?** 
> Yes, the example.txt file

**If the hint above was not provided, what command or ls option(s) could you have run to know what the available options (aka flags) are for the ls command?** 
> `man ls`
> 
> `ls --help`

**Use the next cell to list all files in your SolarSystem folder. What's in there?** 
> Nothing

**What are some other ways you could have written the cp command to copy the Saturn.txt file from your home directory to your SolarSystem folder?**
> `!cp /home/username/Saturn.txt ./`
> 
> `!cp /home/username/Saturn.txt /home/username/SolarSystem/`
> 
> `!cp ../Saturn.txt /home/username/SolarSystem/`

**Can you open up a directory with cat?**
> No

**What happens if you rename a file to a filename that's already in use in the same directory?**
> It will overwrite the file

**What happens if you rename a file to a filename that's already in use in the same directory but when you rename the file, you also move it to a different directory?**
> The file will have the same name but now be located into the directory you moved it to

**What are the options for the cat command?**
>  -A, --show-all           equivalent to -vET
>  
>  -b, --number-nonblank    number nonempty output lines, overrides -n
>  
>  -e                       equivalent to -vE
>  
>  -E, --show-ends          display $ at end of each line
>  
>  -n, --number             number all output lines
>  
>  -s, --squeeze-blank      suppress repeated empty output lines
>  
>  -t                       equivalent to -vT
>  
>  -T, --show-tabs          display TAB characters as ^I
>  
>  -u                       (ignored)
>  
>  -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB
>  
>      --help     display this help and exit
>      
>      --version  output version information and exit

