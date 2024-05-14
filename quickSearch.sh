
# if 2 arguments then we goto
# if 1, we symply show the paths

if [ $# -lt 2 ]; then
    python search.py "$1"
fi

if [ $# -eq 2 ]; then
    python search.py "$1" "$2"
fi

if [ -f "item_path.txt" ]; then
    dir="$(cat item_path.txt)"
    rm "item_path.txt"
    cd $dir 
fi