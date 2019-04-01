
build:
	# Compile everything into a zip file.
	zip -r st.zip .

	echo "#!/usr/bin/python3" | cat - st.zip > st
	chmod a+x st

	rm /usr/bin/st
	mv st /usr/bin/st

	# rm st.zip

	
