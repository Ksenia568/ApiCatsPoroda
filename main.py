import requests

def get_cat_breeds():
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    cat_breeds = get_cat_breeds()

    if cat_breeds:
        for breed in cat_breeds:
            print(f"Порода: {breed['name']}")
            print(f"Описание: {breed['description']}")
            print()
    else:
        print("Информация о породах кошек не найдена.")

if __name__ == "__main__":
    main()






