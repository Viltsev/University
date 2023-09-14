package Task3
import scala.io.StdIn.readLine

object subTask1 {
  def getReversedString(): Unit = {
    println("Задание 1")
    println("Введите строку")
    val string = readLine()
    val result = reverseString(string)
    println(result)
  }

  private def reverseString(string: String): String = {
    // Разделяю строку на слова. В качестве разделителей - пробелы
    val words = string.trim.split("\\s+")
    // Объединяю слова в обратном порядке (reverse)
    // и добавляю между ними по одному пробелу (mkString)
    val reversed = words.reverse.mkString(" ")
    reversed
  }
}

object subTask2 {
  def getReversedString(): Unit = {
    println("Задание 2")
    println("Введите строку")
    val string = readLine()
    val words = string.trim.split("\\s+").toList
    val result = reverseString(words, "")
    println(result)
  }

  private def reverseString(words: List[String], accumulator: String): String = {
    // accumulator - итоговая строка
    // words - список строк (слов из начальной строки)
    // рекурсивно вызываем reverseString,
    // в качестве words - оставшиеся слова (tail),
    // в качестве accumulator - добавляем перед accumulator голову списка
    words match {
      case Nil => accumulator
      case head :: tail => reverseString(tail, head + " " + accumulator)
    }
  }
}

object subTask3 {
  private var result: Float = 0

  def getChipsWeight(withMethod: Boolean): Unit = {
    println("Задание 3")
    println("Введите вес картофеля")
    val potatoWeight = readLine().toFloat
    println("Введите долю воды в картофеле")
    val waterInPotato = readLine().toFloat
    println("Введите долю воды в чипсах")
    val waterInChips = readLine().toFloat

    if (!withMethod) {
      println("Ручное каррирование")
      val addWeight = curriedGetWeightOfChips(potatoWeight) _
      val addWaterInPotato = addWeight(waterInPotato)
      result = addWaterInPotato(waterInChips)

    } else {
      println("Каррирование с помощью функции curried")
      // преобразование обычной функции в каррированную
      val curriedCalculate = (calculateChipsWeight _).curried
      val addWeight = curriedCalculate(potatoWeight)
      val addWaterInPotato = addWeight(waterInPotato)
      result = addWaterInPotato(waterInChips)
    }

    println(f"weight of chips = $result%.2f")
  }

  private def calculateChipsWeight(weight: Float, waterInPotato: Float, waterInChips: Float): Float = {
    (weight * (1 - waterInPotato)) / (1 - waterInChips)
  }

  private def curriedGetWeightOfChips(weight: Float)(waterInPotato: Float)(waterInChips: Float): Float = {
    (weight * (1 - waterInPotato)) / (1 - waterInChips)
  }
}


object task3 extends App {
  subTask1.getReversedString()
  subTask2.getReversedString()
  subTask3.getChipsWeight(false)
}
