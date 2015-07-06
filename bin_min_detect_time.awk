BEGIN{
	FS=":"
}
NR==1{
	d=$1;
	m=$3;
}
{
	if(m>$3 && $3 != 0) {
	    print "detected in" , d , m
		d=$1;
		m=$3;
	}
}
END{
	print "finally at",d,m
}
