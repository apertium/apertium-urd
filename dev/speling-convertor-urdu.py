import sys;

table = {};

for line in open(sys.argv[1]).readlines(): #{

	row = line.split('\t');
	table[row[0].strip()] = row[1].strip();
#}

for line in open(sys.argv[2]).readlines(): #{
	row = line.split(':');

	surf = row[0].strip();	
	lema = row[1].strip();	
	msd = row[2].strip(' -');	

	if msd in table: #{
		print(lema + '; ' + surf + '; ' + table[msd]);
	else: #{
		print('>>>' + lema + ';' + surf + ';' + msd, file=sys.stderr);
	#}
#}
