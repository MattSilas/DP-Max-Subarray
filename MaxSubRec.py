>>> def maxCross(array, low, high, mid):
	ls = rs = -1000
	lp = rp = 0
	curr_sum = 0
	mp = mid
	while mp>=low:
		curr_sum = curr_sum+array[mp]
		if curr_sum>ls:
			ls = curr_sum
			lp = mp
		mp = mp-1
	mp = mid+1
	curr_sum = 0
	while mp<=high:
		curr_sum = curr_sum+array[mp]
		if curr_sum > rs:
			rs = curr_sum
			rp = mp
		mp=mp+1
	return(lp,rp,(ls+rs))

>>> def maxsub(array,low,high):
	if high == low:
		return (low, high, array[low])
	else:
		mid =(low+high)//2
		ll,lh,ls = maxsub(array,low,mid)
		rl,rh,rs = maxsub(array,mid+1,high)
		cl, ch, cs = maxCross(array, low, high, mid)
		if ls>=rs:
			if ls>=cs:
				return (ll,lh,ls)
			else:
				return (cl,ch,cs)
		else:
			if rs>cs:
				return(rl,rh,rs)
			else:
				return(cl,ch,cs)
