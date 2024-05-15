source venv/bin/activate
python ./core/search.py ${@:1}
deactivate

if [ -f "item_path.txt" ]; then
    dir="$(cat item_path.txt)"
    rm "item_path.txt"
    cd $dir 
fi