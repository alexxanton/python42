create_dirs() {
	i=0
	for x in $@; do
		mkdir "ex${i}"
		touch "ex${i}/${x}.py"
		i=$(($i + 1))
	done
}
