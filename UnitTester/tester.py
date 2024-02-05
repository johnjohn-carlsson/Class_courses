from main import Person, PersonRegister
import unittest


class PersonTest(unittest.TestCase):
    def test_when_creating_class_person_to_check_correctly_set_name_and_personnumber(self):
        name = "John-John"
        personnumber = "19921212-1337"

        person = Person(name, personnumber)

        # Kollar om de variabler jag gör Person av faktiskt hamnar i de Person.self värden som jag vill

        self.assertEqual(name, person.Name) # assertEqual kollar om det är likadant värde (==)
        self.assertEqual(personnumber, person.PersonNumber)



class PersonRegisterTest(unittest.TestCase):
    def test_When_fetching_person_correct_person_should_be_returned(self):    
        #arrange    
        person1 = Person("Stefan", "19720803-0000")
        person2 = Person("Kalle", "19790101-0000")
        sut = PersonRegister()
        sut.add(person1)
        sut.add(person2)
        #act
        result = sut.getPerson("19720803-0000")
        #assert
        self.assertEqual(person1, result)

    def test_When_fetching_person_and_person_does_not_exist_correct_errormessage_should_be_returned(self):    
        #arrange    
        person1 = Person("Stefan", "19720803-0000")
        person2 = Person("Kalle", "19790101-0000")
        sut = PersonRegister()
        sut.add(person1)
        sut.add(person2)
        #act
        result = sut.getPerson("19720803-1111")
        #assert
        self.assertEqual("Finns inte", result)


    def test_When_adding_person_and_person_already_exist_correct_errormessage_should_be_returned(self):    
        #arrange    
        person1 = Person("Stefan", "19720803-0000")
        person2 = Person("Kalle", "19720803-0000")
        sut = PersonRegister()
        sut.add(person1)

        #act
        result = sut.add(person2)

        #assert
        self.assertEqual("Duplicate key", result)


if __name__ == "__main__":
    unittest.main()