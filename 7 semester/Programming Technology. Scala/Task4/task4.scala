package Task4
import Task4.subTask2.{Field, Ship, addShipToField}

import scala.io.StdIn.readLine
import scala.collection.immutable

object subTask1 {
  def findOrderStatistic(array: List[Int], k: Int): Unit = {
    val result = findRecursive(0, array.length, array, k - 1)
    println(result)
  }

  private def partition(arr: List[Int], left: Int, right: Int): (List[Int], Int) = {
    var newArray = arr
    val sup = arr(left)
    val subArray = arr.slice(left, right)
    if (subArray.size == 1) {
      (newArray, left)
    } else {
      var sortedSubArray = List.empty[Int]
      val less = subArray.filter(_ < sup)
      val greater = subArray.filter(_ > sup)
      if (less.isEmpty && greater.isEmpty) {
        sortedSubArray = subArray
      } else {
        sortedSubArray = less ::: (sup :: greater)
      }
      for (i <- left until right) {
        newArray = newArray.updated(i, sortedSubArray(i - left))
      }
      val mid = newArray.indexOf(sup)
      (newArray, mid)
    }
  }

  private def findRecursive(left: Int, right: Int, array: List[Int], k: Int): Int = {

    val (newArray, mid) = partition(array, left, right)

    if (mid == k) {
      newArray(mid)
    } else if (k < mid) {
      findRecursive(left, mid, newArray, k)
    } else {
      findRecursive(mid + 1, right, newArray, k)
    }
  }

}

object subTask2 {
  type Point = (Int, Int)
  type Ship = List[Point]
  type Field = Vector[Vector[Boolean]]

  def addShipToField(field: Field, ship: Ship): Field = {
    // Проверка на то, что корабль полностью помещается на поле
    val shipFitsOnField = ship.forall { case (x, y) =>
      x >= 0 && x < 10 && y >= 0 && y < 10
    }

    if (shipFitsOnField) {
      var newField = field
      for (i <- field.indices) {
        for (j <- field.indices) {
          if (ship.contains((i, j))) {
            val newVector = newField(i).updated(j, true)
            newField = newField.updated(i, newVector)
          }
        }
      }
      newField
    } else {
      // Если корабль не помещается на поле, просто вернуть исходное поле без изменений
      field
    }
  }
}

object task4 extends App {

  private def seaBattle(): Unit = {
    val initialField: Field = Vector.fill(10, 10)(false)
    println("Initial Field")
    for (coor <- initialField) {
      println(coor)
    }

    println("Enter ship's coordinates: ")
    print("First: ")
    val coor1 = readLine.split(' ').map(_.toInt)
    print("Second: ")
    val coor2 = readLine.split(' ').map(_.toInt)
    print("Third: ")
    val coor3 = readLine.split(' ').map(_.toInt)
    val shipToAdd: Ship = List((coor1(0), coor1(1)),
                               (coor2(0), coor2(1)),
                               (coor3(0), coor3(1))
                              )
    val updatedField = addShipToField(initialField, shipToAdd)
    println("Updated Field")
    for (coor <- updatedField) {
      println(coor)
    }
  }

  private def threeLists(): Unit = {

    val list1 = List(1, 2, 3, 4)
    val list2 = List(2, 3, 4, 5)
    val list3 = List(2, 6, 8, 12)

    var resultPairs = List.empty[(Int, Int)]

    resultPairs = for {
      x <- list1
      y <- list2
      if x != y
      z <- list3
      if x * y == z
    } yield (x, y)

    val sortedPairs = resultPairs.sorted

    sortedPairs.foreach(pair => println(pair))
  }

  println("CHOOSE TASK WHAT YOU WANT TO RUN:")
  println("1. k-statistic\n2. sea battle\n3. three lists")
  val task = readLine().toInt
  task match {
    case 1 => subTask1.findOrderStatistic(List(4, 7, 6, 5, 12, 9, 5), 5)
    case 2 => seaBattle()
    case 3 => threeLists()
  }
}
// subTask1.findOrderStatistic(List(4, 7, 6, 5, 12, 9, 5), 3) -> 5
// subTask1.findOrderStatistic(List(3, 8, 1, 12, 23), 4) -> 12
// subTask1.findOrderStatistic(List(4, 7, 6, 5, 12, 9, 5), 5) -> 7