# BIG DTA
            Nama  : Annisa Fitri Yuliandra
            NIM   : 2041720123
            Kelas : TI 3B
            Prodi : D4 Teknik Informatika

---
## Accumulator
![](Accumulator\1.png)
- Pada baris pertama kode, objek myaccum dibuat sebagai variabel accumulator yang bernilai awal nol (0). Accumulator adalah variabel yang dapat diakses oleh setiap worker pada Spark, dan nilainya dapat ditingkatkan secara bersamaan oleh worker yang berbeda.

- Selanjutnya, pada baris kedua, sebuah RDD (Resilient Distributed Dataset) dibuat dengan nama myrdd yang berisi bilangan bulat dari 1 hingga 99. RDD adalah dasar dari pemrograman Spark dan mewakili kumpulan item yang didistribusikan secara terdistribusi di beberapa mesin.

- Pada baris ketiga, fungsi foreach diterapkan pada RDD myrdd, yang akan melakukan operasi untuk setiap elemen dalam RDD tersebut. Dalam kasus ini, fungsi foreach menerapkan sebuah lambda expression atau fungsi anonim yang melakukan penambahan pada nilai accumulator myaccum dengan setiap elemen dalam RDD myrdd.

- Pada baris terakhir, hasil akhir dari accumulator diambil dengan memanggil myaccum.value dan mencetaknya ke konsol. Hasil akhirnya adalah jumlah dari kumpulan bilangan bulat dari 1 hingga 99, yang seharusnya bernilai 4950.

## Broad Cast
![](BroadCast\2.png)
- Pada baris pertama kode, objek broadcastVar dibuat sebagai variabel broadcast yang berisi daftar bilangan bulat dari 1 hingga 99. Variabel broadcast adalah cara untuk menyebarkan variabel yang tidak berubah kepada semua worker pada Spark secara efisien, sehingga setiap worker dapat mengaksesnya tanpa harus memuat variabel tersebut ke dalam memori lokal.

- Pada baris kedua, nilai dari variabel broadcast diambil dengan memanggil broadcastVar.value, yang akan mengembalikan nilai asli dari variabel broadcast. Dalam hal ini, nilai yang dikembalikan adalah daftar bilangan bulat dari 1 hingga 99 yang sudah disebarkan kepada semua worker pada Spark.

- Hasil dari kode tersebut akan mencetak daftar bilangan bulat dari 1 hingga 99 ke konsol. Perlu diperhatikan bahwa variabel broadcast hanya berguna untuk variabel yang tidak berubah, seperti dalam kasus ini, daftar bilangan bulat yang tetap. Jika variabel berubah atau diubah nilai selama program berjalan, maka variabel broadcast tidak dapat digunakan.

## Log Analytics
![](LogAnalytics\1.png)
- Pada baris pertama kode, file teks "pendidikan.txt" dibaca menggunakan fungsi textFile pada Spark, dan dibagi menjadi 4 partisi. textFile akan mengembalikan RDD yang mewakili baris-baris dalam file teks sebagai elemen RDD.

- Pada baris kedua, RDD yang diberi nama access_log difilter menggunakan fungsi filter dengan kondisi hanya baris yang mengandung kata "tinggi" yang akan dipertahankan dalam RDD.

- Pada baris ketiga, hasil filter sebelumnya yang disimpan di dalam variabel error_log dicache di dalam memori dengan memanggil fungsi cache. Hal ini dilakukan untuk mengoptimalkan performa, sehingga RDD tidak perlu dikomputasi ulang setiap kali dibutuhkan.

- Pada baris keempat, sebuah aksi dilakukan dengan memanggil fungsi count pada variabel cached_log. Fungsi count mengembalikan jumlah elemen dalam RDD. Hasilnya dicetak ke konsol.

- Pada baris kelima, fungsi count kembali digunakan untuk menghitung jumlah baris pada RDD cached_log yang mengandung kata "pendidikan".

- Hasil dari kode tersebut adalah dua nilai jumlah baris yang dicetak ke konsol: total jumlah baris pada file pendidikan.txt yang mengandung kata "tinggi" dan jumlah baris pada file yang juga mengandung kata "pendidikan".

## Pair RDD
![](PairRDD\3.png)
- Pada baris pertama, sebuah list dengan nama mylist yang berisi tiga string yaitu "my", "pair", dan "rdd" dibuat.

- Pada baris kedua, list tersebut diubah menjadi RDD dengan memanggil fungsi parallelize pada objek sc (SparkContext) pada Spark.

- Pada baris ketiga, RDD yang dibuat pada baris sebelumnya diubah menjadi Pair RDD dengan memanggil fungsi map pada RDD. Fungsi map pada RDD digunakan untuk melakukan transformasi pada setiap elemen RDD. Dalam kasus ini, setiap elemen RDD diubah menjadi tuple (pasangan) yang berisi string itu sendiri dan panjang stringnya. Hasilnya adalah Pair RDD yang terdiri dari tiga pasangan tuple (key, value) yaitu ("my", 2), ("pair", 4), dan ("rdd", 3).

- Pada baris keempat, sebuah aksi dilakukan dengan memanggil fungsi collect pada variabel myPairRDD. Fungsi collect mengembalikan seluruh elemen dari RDD dan mengumpulkannya ke dalam bentuk list pada driver program. Pada kasus ini, fungsi collect akan mengembalikan seluruh pasangan tuple dalam myPairRDD dan dicetak ke konsol.

- Pada baris kelima, fungsi keys digunakan untuk mengembalikan seluruh key dari setiap pasangan tuple dalam myPairRDD dan mengumpulkannya ke dalam bentuk list. Pada kasus ini, fungsi keys akan mengembalikan list ['my', 'pair', 'rdd'] dan dicetak ke konsol.

- Pada baris terakhir, fungsi values digunakan untuk mengembalikan seluruh value dari setiap pasangan tuple dalam myPairRDD dan mengumpulkannya ke dalam bentuk list. Pada kasus ini, fungsi values akan mengembalikan list [2, 4, 3] dan dicetak ke konsol.

## System Commands Output
![](SystemCommandsOutput\4.png)
- Pada baris pertama, operator import digunakan untuk mengimpor package sys.process._ yang berisi kelas-kelas untuk menjalankan proses operasi sistem pada Scala.

- Pada baris kedua, sebuah variabel output dibuat dengan memanggil command Hadoop hadoop fs -ls menggunakan operator !!. Operator !! pada Scala digunakan untuk mengeksekusi command pada terminal dan mengembalikan output dari command tersebut.

- Pada baris ketiga, output dari command Hadoop tersebut dicetak ke konsol menggunakan fungsi println. Output tersebut berisi informasi mengenai isi dari direktori yang aktif pada HDFS. Informasi tersebut dapat berupa nama file, ukuran file, tanggal pembuatan, dan hak akses.

## System Commands Return Code 
![](SystemCommandsReturnCode\5.png)
![](SystemCommandsReturnCode\6.png)
- Pada baris pertama, operator import digunakan untuk mengimpor package sys.process._ yang berisi kelas-kelas untuk menjalankan proses operasi sistem pada Scala.

- Pada baris kedua, sebuah variabel res dibuat dengan memanggil command sistem ls /tmp menggunakan operator !. Operator ! pada Scala digunakan untuk mengeksekusi command pada terminal dan mengembalikan nilai integer yang menunjukkan status exit dari command tersebut. Jika command berhasil dieksekusi, maka nilai integer yang dikembalikan adalah 0. Namun jika command gagal dieksekusi, maka nilai integer yang dikembalikan adalah nilai non-zero yang menunjukkan jenis error yang terjadi.

- Pada baris ketiga, status exit dari command ls /tmp dicetak ke konsol menggunakan fungsi println. Jika command berhasil dieksekusi, maka nilai yang dicetak adalah result = 0. Namun jika command gagal dieksekusi, maka nilai yang dicetak adalah result = [nilai non-zero].

## Understanding RDD
![](UndersandingRDDs\1.png)
- Pada baris pertama, sc.defaultParallelism digunakan untuk mengecek jumlah partisi default yang digunakan oleh Spark.

- Kemudian pada baris ke-5 dan ke-7, sebuah list myList dijalankan dan kemudian diubah menjadi RDD dengan menggunakan sc.parallelize(). Pada baris ke-6 dan ke-8, getNumPartitions() digunakan untuk mengecek jumlah partisi pada RDD yang telah dibuat.

- Pada baris ke-11, count() digunakan untuk menghitung jumlah elemen pada RDD.

- Pada baris ke-14 dan ke-18, mapPartitionsWithIndex() digunakan untuk menampilkan data dalam setiap partisi dari RDD. mapPartitionsWithIndex() menerima fungsi yang menerima dua argumen, yaitu index partisi dan iterator data di partisi tersebut.

- Pada baris ke-22 dan ke-26, repartition() dan coalesce() digunakan untuk mengubah jumlah partisi dari RDD. repartition() digunakan untuk meningkatkan jumlah partisi, sedangkan coalesce() digunakan untuk mengurangi jumlah partisi. Setelah diubah jumlah partisinya, kembali ditampilkan data dalam setiap partisi dengan menggunakan mapPartitionsWithIndex().

- Pada baris ke-30, toDebugString() digunakan untuk menampilkan lineage graph dari RDD. Lineage graph merupakan representasi visual dari RDD dan operasi-operasi yang telah dijalankan pada RDD tersebut.

## Word Count
![](WordCount\7.png)
- Pertama, file teks dibaca dengan menggunakan sc.textFile(), dan dimuat ke dalam RDD.

- Kemudian, tiap baris pada RDD tersebut dipecah-pecah menjadi kata-kata dengan menggunakan flatMap() dan dipetakan ke tuple (kata, 1) dengan map().

- Selanjutnya, kata-kata yang sama dijumlahkan dengan reduceByKey(), dengan menggabungkan tuple-tuple yang memiliki kunci yang sama.

- Akhirnya, hasil hitungan diambil dengan collect(), dan kemudian ditampilkan pada layar dengan menggunakan print().