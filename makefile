ARGS = "decode YDQEQGASQGDKVTMKLDQEVTDKVT PLAYFIREXMBCDGHKNOQSTUVWZ"
all:
	python3 vigenere.py $(ARGS)
run:
	python3 vigenere.py $(ARGS)