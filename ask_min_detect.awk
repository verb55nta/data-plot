BEGIN{
	FS=":"
}
NR==1{
	d=$1;
	m=$5;
}
{
	if(m>$5) {
		d=$1;
		m=$5;
	}
}
END{
	print d,m
}
