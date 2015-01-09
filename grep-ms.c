#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libms.h"

int count_elements(char *buf);

int main()
{
	int X, Ceilings;
	ms_state_t st;
	int *ms;
	char *buf;

	buf=malloc(0xffff*sizeof(char));
	if(buf==NULL)
		return 1;

	if((buf=fgets(buf, 0xffff, stdin))==NULL)
		return 0;

	Ceilings=count_elements(buf);
	X=sqrt(Ceilings);

	ms_init(X, MS_ORIGIN_ONE, &st);

	do{
		ms=str_to_ms(buf, &st);
		if(is_ms(ms, &st)==MS_TRUE)
			fputs(buf, stdout);
	}while(fgets(buf, 0xffff, stdin)!=NULL);

	ms_finalize(&st);
	
	return 0;
}

int count_elements(char *buf)
{
	int c;
	char *endptr;

	for(c=0; ; c++, buf=endptr){
		strtol(buf, &endptr, 10);
		if(buf==endptr)
			break;
	}
	
	return c;
}
