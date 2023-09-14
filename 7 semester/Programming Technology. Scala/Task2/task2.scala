package Task2
import scala.io.StdIn.readLine

object subTask1 {
  private var count = 0
  println("Задание 1")
  println("Введите целое число для подсчета числа единиц в битовой записи")
  private val number = readLine().toInt.toBinaryString

  def countsOnes(): Unit = {
    for (i <- number)
      if (i == '1')
        count += 1

    println(count)
  }
}

object subTask2 {
  private var counter = 1
  println("Задание 1")
  println("Введите натуральное число n")
  private val n = readLine().toInt

  def getLadder(): Unit = {
    while (counter != n + 1) {
      var subCounter = 0
      while (subCounter != counter) {
        subCounter += 1
        print(s"${subCounter} ")
      }
      println()
      counter += 1
    }
  }
}

object subTask3 {
  println("Задание 1")
  println("Введите строку для определения на snake case")
  private var string = readLine()

  def defineSnakeCase(): Unit = {
    while (string != "") {
      println(snake_case(string))
      string = readLine()
    }
  }

  private def snake_case(str: String): Boolean = {
    val stringPattern = "^[a-z]+(_[a-z]+)*".r
    str match {
      case stringPattern(_) => true
      case _ => false
    }
  }
}

object task2 extends App {
  // Задание 1. Напишите программу для подсчета числа единиц
  // в битовой записи целого числа, считанного с клавиатуры
    subTask1.countsOnes()

  // Задание 2. Напишите программу, которая вводит n - натуральное число.
  // Выводит на экран лесенку
    subTask2.getLadder()
  // Задание 3. Напишите метод для определения, является ли переданная строка
  // записанной в snake-case стиле.
    subTask3.defineSnakeCase()
}