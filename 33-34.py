# задача 1

import json

users = []

for element in range(3):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    user = {}
    user['name'] = name
    user['age'] = age
    print(user)
    users.append(user)
print('\n', users)

with open('users.json.py', mode='w') as f:
    json.dump(users, f, indent=2)

# задача 2

with open('users.json.py', mode='r') as f:
	users = json.load(f)
	max_age = 0
	for user in users:
		if int(user['age']) > max_age:
			max_age = user['age']
	print(f'\nМаксимальный возраст пользователя: {max_age}')

# задача 3

filename = 'notes.json'

def print_notes(filename):
	with open(filename, mode='r') as f:
		notes = json.load(f)
		for note in notes:
			print(f"{note['id']}.", note['name'], note['text'])

def add_note(filename):
	with open(filename, mode='r') as f:
		notes = json.load(f)
	name = input('Введите название заметки: ')
	text = input('Введите текст заметки: ')

	note = {}
	note['name'] = name
	note['text'] = text

	notes.append(note)

	for note_id, note in enumerate(notes):
		note['id'] = note_id + 1

	with open(filename, mode='w') as f:
		json.dump(notes, f, indent=2)

def read_note(filename):
	with open(filename, mode='r') as f:
		notes = json.load(f)

	note_id = int(input('Введите id заметки для чтения: '))
	for note in notes:
		if note.get('id') == note_id:
			print(f"{note['id']}.", note['name'], note['text'])

def remove_note(filename):
	note_id = int(input('Введите id заметки для удаления: '))
	with open(filename, mode='r') as f:
		notes = json.load(f)
	for note in notes:
		if note.get('id') == note_id:
			notes.remove(note)

	for note_id, note in enumerate(notes):
		note['id'] = note_id + 1
	with open(filename, mode='w') as f:
		json.dump(notes, f, indent=2)

while True:
	print("\nВыберите действие:")
	print("1. Показать все заметки")
	print("2. Добавить заметку")
	print("3. Прочитать заметку")
	print("4. Удалить заметку")
	print("5. Выход")
	choice = input("> ")

	if choice == "1":
		print_notes(filename)
	elif choice == "2":
		add_note(filename)
	elif choice == "3":
		read_note(filename)
	elif choice == "4":
		remove_note(filename)
	elif choice == "5":
		break
	else:
		print("Некорректный выбор.")