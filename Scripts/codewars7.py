def sort_by_length(arr):
    dict_pal = dict([
                (len(pal),pal)
                for pal in arr 
        ])
    return [dict_pal[key] for key in sorted(dict_pal.keys())]   
print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))