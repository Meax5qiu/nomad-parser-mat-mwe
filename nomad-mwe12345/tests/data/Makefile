testall: dump-contents

# Create example Matlab output file, Matlab call
#struct.mat:
#	matlab -r     "mainstruct.data.float = 3.4; mainstruct.data.arr = [5 -2]; mainstruct.meta.str = 'verbatim'; save('$@', 'mainstruct');"

# Create example Matlab output file, Octave call
struct.mat:
	octave --eval "mainstruct.data.float = 3.4; mainstruct.data.arr = [5 -2]; mainstruct.meta.str = 'verbatim'; save('$@', '-v6', 'mainstruct');"

# Display contents of the Matlab file
.PHONY: dump-contents
dump-contents: struct.mat
	./display_matlab_dump.py $<
