from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)

def grammar(prompt):
    input = "grammar: "+prompt
# Add the prefix "grammar: " before each input 
    result = happy_tt.generate_text(input, args=args)
    return result.text

#prompt = input("Enter something")
#print(grammar(prompt))

