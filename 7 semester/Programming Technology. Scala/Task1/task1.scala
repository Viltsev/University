package Task1
import scala.io.StdIn.readLine

object task1Extension {
  import Config.{name => prefix}
  def greeting(name: String) {
    println(prefix + name);
  }
}

object task1 extends App {
  // Задание 1. Напишите программу для ввода трех чисел с консоли и вывода на экран их произведения
  println("Задание 1")
  println("Введите три числа через пробел")
  private val numbers = readLine.split(' ').map(_.toInt)
  println(numbers(0) * numbers(1) * numbers(2))

  // Задание 2
  println("Задание 2")
  task1Extension.greeting("Anna")

  // Задание 3. Реализуйте метод подсчета веса чипсов
  println("Задание 3")
  println("Введите: Вес картофеля | Доля воды в картофеле | Доля воды в чипсах")
  private val chipsArray = readLine.split(' ').map(_.toFloat)
  private val chipsWeight = (chipsArray(0) * (1.0 - chipsArray(1))) / (1 - chipsArray(2))
  println(f"$chipsWeight%.2f")
}