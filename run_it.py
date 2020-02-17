from ceasar_exercise.encrypt import encrypt as e
from ceasar_exercise.decrypt import decrypt as d

my_plain_text = e("a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z", -7)
print(my_plain_text)
my_ceasar = d(my_plain_text, -7)
print(my_ceasar)