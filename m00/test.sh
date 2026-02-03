path="ex${1}"

tests() {
	cp main.py "${path}/m.py"
	cd $path
	python3 m.py $1
	rm "m.py"
	rm -rf __pycache__
}

if [[ $path == "exa" ]]; then
	for x in {0..7}; do
		path="ex${x}"
		tests $x
		cd ..
	done
else
	tests $1
fi
