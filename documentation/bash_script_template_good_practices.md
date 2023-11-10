A sample bash script template that has some good practices built in: (from https://sharats.me/posts/shell-script-best-practices/)

```bash
#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
    set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
    echo 'Usage: ./script.sh arg-one arg-two

This is an awesome bash script to make your life better.

'
    exit
fi

cd "$(dirname "$0")"

main() {
    echo do awesome stuff
}

main "$@"

```

explaination:
- `set -o errexit`: when a command fails, bash exits instead of continuing with the rest of the script
- `set -o nounset`:  script will fail if you try to access an unset variable
- `set -o pipefail`: ensure a pipeline command will fail if one of the steps fail
- `if [[ "${1-}" =~ ^-*h(elp)?$ ]]; ...` : this allows other people to run `script.sh --help` and it will spit out help info
- `cd "$(dirname "$0")"`:  change to the script’s directory 
- 
