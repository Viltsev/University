package Steganography
import java.io.{File, FileReader, FileWriter, RandomAccessFile}
import java.nio.file.{Files, Paths}

object SteganographyDecoder {
  val RUS_LETTERS = "аеорсухАВЕКМНОРСТХ"
  val ENG_LETTERS = "aeopcyxABEKMHOPCTX"

  def decode(messagePath: String, stegocontainerPath: String): Unit = {
    val stegocontainer = new FileReader(stegocontainerPath)
    val message = new RandomAccessFile(messagePath, "rw")

    var bitsRead = 0
    var byte = 0
    var lastSymbolPosition = 0

    try {
      while (true) {
        val symbol = stegocontainer.read()
        if (symbol == -1) {
          return
        }

        val symbolChar = symbol.toChar
        if (ENG_LETTERS.contains(symbolChar)) {
          byte <<= 1
          bitsRead += 1
        } else if (RUS_LETTERS.contains(symbolChar)){
          byte <<= 1
          byte |= 1
          bitsRead += 1
        }

        if (bitsRead == 8) {
          message.write(byte.toByte)
          if (lastSymbolPosition > 0) {
            lastSymbolPosition += 1
          }
          if (byte.toChar == '@') {
            lastSymbolPosition = 1
          }

          bitsRead = 0
          byte = 0
        }
      }
    } finally {
      if (lastSymbolPosition > 0) {
        val messageLength = message.length()
        val newPosition = messageLength - lastSymbolPosition
        message.seek(newPosition)
        message.setLength(newPosition)

        stegocontainer.close()
        message.close()
      } else {
        stegocontainer.close()
        message.close()
      }
    }
  }
}
