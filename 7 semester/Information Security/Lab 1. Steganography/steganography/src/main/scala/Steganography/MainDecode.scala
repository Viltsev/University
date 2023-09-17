package Steganography

object MainDecode extends App {
  val parser = new scopt.OptionParser[Config]("SteganographyDecoder") {
    head("SteganographyDecoder", "1.0")

    opt[String]('m', "message")
      .action((x, c) => c.copy(messagePath = x))
      .text("Путь к файлу, в который нужно записать сообщение в том виде, в котором оно было до встраивания. Если не указан, то сообщение выводится в стандартный поток вывода.")

    opt[String]('s', "stego")
      .action((x, c) => c.copy(stegocontainerPath = x))
      .text("Путь к стегоконтейнеру. Если не указан, то содержимое стегоконтейнера передаётся через стандартный поток ввода.")
  }

  parser.parse(args, Config()) match {
    case Some(config) =>
      try {
        SteganographyDecoder.decode(config.messagePath, config.stegocontainerPath)
      } catch {
        case e: Exception =>
          println("Кажется, что-то пошло не так...")
          e.printStackTrace()
      }
    case None => println("None")
  }
}
