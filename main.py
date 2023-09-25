meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey.",
            "LOL": "Sesli Gülmek",
            "HILMIII" : "ℌ𝔦𝔩𝔪𝔦.",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
 
 
if word in meme_dict.keys():
     print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("üzgünüm aratdığınız kelime listemizde yok.")
