def brute_force():
	msg = raw_input('Enter your text here: ')

	key = len(msg)/2

	alphabets = 'ABC2&0346_+/*~DEFGHIJK(){";.<.>LMNOPQRST:?UVWXYZ!#$%'
	cipher = ''

	msg = msg.upper()

	for chars in msg:
		if chars in alphabets:
			sol = alphabets.find(chars)
			sol = sol + key

			if sol >= len(alphabets):
				sol = sol - len(alphabets)

			elif sol < 0:
				sol = sol + len(alphabets)

			cipher = cipher + alphabets[sol]

		else:
			cipher = cipher + chars
	print('Encrypted text {}'.format(cipher))
	decrypt = cipher

	word = 'Couldnt find'

	for key in range(len(alphabets)):
		dec_text = ''

		for alphas in decrypt:
			if alphas in alphabets:
				sol_dec = alphabets.find(alphas)
				sol_dec = sol_dec - key 

				if sol_dec < 0:
					sol_dec = sol_dec + len(alphabets)

				dec_text = dec_text + alphabets[sol_dec]

			else:
				dec_text = dec_text + alphas

		print('key {} {}'.format(key, dec_text))

		if (dec_text == msg.upper()):
			word = dec_text


	print('Decrypted text is {}, you can also see this when key is {key}'.format(word.lower(), key = len(msg)/2)) 
brute_force()
