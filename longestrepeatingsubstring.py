stri = "DVYCNZVJIHNVMNBDFTRRSNNXPIRMFMZZOYUFXGBEHKEVDDFVMTURWDAXMDGKMZBIOJZFOZLZOHLGVMFVBIQEPOUZOBCRSOVTVGNIUJVEUZEVTOZVPIFYPMRZUCBLHCGZXJHCENNZMVOFVONCJOGCFVAUTZRKIZJRUZEPQVEKPAGYFRBIMYVKJNNNBTVYBQRFGYEZWDAXPASKIZFGMZREBIQIFBHCBOVEHOUVDDETVGNKJJANIZAVWZEZGDAUNTFVMATIPRVEHBEZNVOFVOGYFHBLUCJYFIRMFMVKJNNUBHCUSDMQMTAFWZZSFMVENTFFVGJYFIRMFMVWJIQDZNRCGDAMPGHEUVEZMTCRVNVEHWRWPMRTPASZORNIFCBLTZFROYOIJITZOBHGUCRIFVEFGZIVSTSLOZERMDZVFONEEZFGFXVRMGLNIZAVWZEDZCLGPNTVUNHTIVALQKRIIVAUPAZVUCNKJOEVRPVIFNNJUMBEHHBIBGCIJIPZQGRKPKEVWZAKNZSIPHQVMDOVSVGVMTFKFKCZOBVEUJGYFNGIFZGROYZVUCBUJXNCMTXEPXXZOBCVPKYVTCNKTJSWUCREJVPTPPAKJOUZHCGZNZGFHZGKPNRRBNFFPINJJXNEUCVJJNZPTPOJUDGLUZSFSKVJUJYROYORMGJZUCNGIDYFTJCYJXNCGGBLSDFYDVGFUCEFXNUZNNRCGPCFOCVJTRBIEDDLJZGCZONBFOBKIZFYJKGYFMRZTIBKIDAXTPEGSDFZOBVEUCVJJAGYFTOLUFAVXDGRMHBJUVYCNZAZOOUVJMQVHMRVTJZVUDZVPMBKIZETIZEZTCIVSTAVBMYPUCRJBHRWFZYZOBFKPRNIENGYFJPVBIJZUCZVUCRIFIBNJNLFVMVETPYRSXVKZJSKIZZROCNKUJRJCZYKFYEFVIQSZRURSQRJBNVEEDNEJNYVTWLTPMNCSZRWTXBDNZETFNHISJHEENVKXDGYIZEJVMSIJBUKBIQCFAGKIZFKSZRKTONBFTBLXVGVSRNIEDGJFSGIFHRUPRAKPRAZTOUVCVGKFMLNIZEVUCNKOJOCFHBCFDFNBNUVEWLNBQRJBIQTPJYVEWLSSZRQFNJYJXURGZJYPPEJQMRMJJHJXZEVPPGFGNVXIOBWMVAUMJBBBOGYFXEFXYFFGRNKFMTRAZEJUCRIF"

alphabet = 'abcdefghijklmnopqrstuvwxyz'


frequencyDict = {}
for char in alphabet:
    frequencyDict[char] = 0

charcount = 0
for char in stri.lower():
    #print("hi")
    if charcount%4 == 3 and char in frequencyDict:
        frequencyDict[char]+=1
    charcount+=1

print("Character frequencies:")
for key in frequencyDict:
    frequencyDict[key]/=charcount/4
    print(key,frequencyDict[key])