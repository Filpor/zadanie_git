print("Lista Zakupów")
shop_dictionary= {
    "piekarnia": ["chleb","bulki","paczek"],
    "warzywniak": ["rukola","seler","marchew"]
}
for key, value in shop_dictionary.items():
    print ("Idę do", key.capitalize() , "kupiuję", value)
values_tab1=shop_dictionary.get("piekarnia")
values_tab2=shop_dictionary.get("warzywniak")
print("kupię", len(values_tab1+values_tab2) , "produktów")