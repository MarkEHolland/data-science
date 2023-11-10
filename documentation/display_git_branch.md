It can be very useful to display the current git branch you are working on in the terminal. You can do this by adding this function to your .bashrc file

```bash
show_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
```

then add to:

```bash
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(show_git_branch)\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(show_git_branch)\$ '
fi
```

(obviously remember to add the function above where you are using it)

`PS1` is a special variable to store the terminal prompt format.

Or you can install oh-my-zsh :)
