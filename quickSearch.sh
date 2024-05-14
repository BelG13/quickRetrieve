python search.py ${@:1}

if [ -f "item_path.txt" ]; then
    dir="$(cat item_path.txt)"
    rm "item_path.txt"
    cd $dir 
fi