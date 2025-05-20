for _ in range(int(input())):
	n = int(input())
	s = '0' + input()
	a = [0] + list(map(int, input().split()))
	ans = 0
	i = 0
	while i <= n:
		mn = a[i]
		sm = a[i]
		j = i + 1
		while j <= n and s[j] == '1':
			mn = min(mn, a[j])
			sm += a[j]
			j += 1
		ans += sm - mn
		i = j
	print(ans)