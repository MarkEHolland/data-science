**Some really useful links:**
- https://explainshell.com/ for understanding what all those mysterious stack overflow answers really mean
- https://datascienceatthecommandline.com/2e/ a really good book which teaches how to  work with data just using the terminal 

**A few 'standard' commands I use all the time:**
- `head`/ `tail` for examing a few lines of a large files/get the column names or delimitter
- `less` to page through a file 
- `> /dev/null` to pipe unneccessary output to temp file (e.g. if you are running ! commands in notebooks and don't want to keep the output)
- `history | grep [some_command_name]` to find all the variations of `[some_command_name]` you have done before (useful for commands that have a lot of arguments e.g. docker build xxxx)
- `&&` for chaining commands together
- cat `xxx_filename` | wc -l for how many lines a file have (e.g. if you need to sample data, check if pandas is reading correctly etc)
- the human readable option: `du --human-readable` will list all the files and their sizes in the directory you are running this from (useful to find mysterious memory hogging files, especially if they are 'hidden' files, and also faster to check file size without having to leave your IDE/notebook)
