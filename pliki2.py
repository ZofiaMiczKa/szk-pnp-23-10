import chardet # biblioteka sluzy do rozszyfrowania kodowania

#pip install chardet w terminalu

file_path ="test.log"

with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# przy odpowiednio duzej probce dostajemy wlasciwe kodowanie
# {'encoding': 'utf-8', confience

encoding = result['encoding']
print(encoding)

print(raw_data.decode(encoding=encoding))
