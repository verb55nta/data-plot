BEGIN{
	FS=":"
}
NR==1{
	d=$1;
	m=$5;
}
{
	if(m>$5 && $5 != 0) {
	    print "detected in",d,m
		d=$1;
		m=$5;
	}
}
END{
	print "finally at",d,m
}
