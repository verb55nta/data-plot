BEGIN{
	FS=":"
}
NR==1{
	d=$1;
	m=$3;
}
{
	if(m>$3) {
		d=$1;
		m=$3;
	}
}
END{
	print d,m
}
