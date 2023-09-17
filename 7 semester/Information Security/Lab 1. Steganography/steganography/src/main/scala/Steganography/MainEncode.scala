package Steganography
import java.io.{File, FileWriter, FileReader}

object MainEncode extends App {
  val parser = new scopt.OptionParser[Config]("SteganographyEncoder") {
    head("SteganographyEncoder", "1.0")

    opt[String]('m', "message")
      .action((x, c) => c.copy(messagePath = x))
      .text("Путь к файлу, содержащему сообщение. Если не указан, то сообщение передаётся через стандартный поток ввода.")

    opt[String]('s', "stego")
      .action((x, c) => c.copy(stegocontainerPath = x))
      .text("Путь по которому нужно записать стегоконтейнер. Если не указан, то результат выводится в стандартный поток вывода.")

    opt[String]('c', "container")
      .required()
      .action((x, c) => c.copy(containerPath = x))
      .text("Путь к файлу-контейнеру. Обязательный параметр!")
  }

  parser.parse(args, Config()) match {
    case Some(config) =>
      try {
        SteganographyEncoder.encode(config.messagePath, config.containerPath, config.stegocontainerPath)
      } catch {
        case e: Exception =>
          println("Кажется, что-то пошло не так...")
          e.printStackTrace()
      }
    case None => println("None")
  }
}

