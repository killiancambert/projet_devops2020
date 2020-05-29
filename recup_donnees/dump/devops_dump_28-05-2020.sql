-- MariaDB dump 10.17  Distrib 10.4.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: devops
-- ------------------------------------------------------
-- Server version	10.4.6-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `devops`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `devops` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `devops`;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data` (
  `numero_unite` int(2) NOT NULL,
  `numero_automate` int(2) NOT NULL,
  `type_automate` varchar(10) NOT NULL DEFAULT '9999999999',
  `temperature_cuve` float NOT NULL DEFAULT 99.99,
  `temperature_exterieur` float NOT NULL DEFAULT 99.99,
  `poids_lait_cuve` int(4) NOT NULL DEFAULT 10000000,
  `poids_produit_fini` int(2) NOT NULL DEFAULT 10000000,
  `pH` float NOT NULL DEFAULT 9999.9,
  `K` int(2) NOT NULL DEFAULT 99,
  `NaCl` float NOT NULL DEFAULT 9999.9,
  `salmonelle` int(2) NOT NULL DEFAULT 99,
  `Ecoli` int(2) NOT NULL DEFAULT 99,
  `listeria` int(2) NOT NULL DEFAULT 99,
  `dateheure` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES (1,1,'0X0000BA20',3.8,12.9,4537,443,6.9,43,1.6,17,41,46,'28-05-2020 09:03:49'),(1,2,'0X0000BA20',2.9,10.8,3856,739,6.8,45,1.4,37,39,46,'28-05-2020 09:03:49'),(1,3,'0X0000BA20',3,10.7,4100,224,6.9,35,1.2,36,46,38,'28-05-2020 09:03:49'),(1,4,'0X0000BA20',3.4,11.8,4220,95,7,42,1.1,30,39,46,'28-05-2020 09:03:49'),(1,5,'0X0000BA2F',3.6,11.8,3706,577,7,42,1.1,26,44,38,'28-05-2020 09:03:49'),(1,6,'0X0000BA20',3.6,8.5,4222,881,7.2,36,1.2,25,49,51,'28-05-2020 09:03:49'),(1,7,'0X0000BA20',3.5,12.4,3905,1030,6.8,37,1.2,30,39,41,'28-05-2020 09:03:49'),(1,8,'0X0000BA2F',3.3,13.7,3538,322,6.9,44,1.1,28,36,45,'28-05-2020 09:03:49'),(1,9,'0X0000BA2F',3.4,12.1,3778,1017,6.9,38,1.1,35,41,52,'28-05-2020 09:03:49'),(1,10,'0X0000BA2F',3.4,11.8,3680,808,7,42,1.2,36,36,40,'28-05-2020 09:03:49'),(2,1,'0X0000BA20',2.8,9,4125,73,7.1,42,1.6,29,39,41,'28-05-2020 09:03:49'),(2,2,'0X0000BA20',3.3,11.1,3852,80,6.8,38,1,18,42,42,'28-05-2020 09:03:49'),(2,3,'0X0000BA2F',3.3,10.2,3841,802,7.1,44,1.2,30,42,39,'28-05-2020 09:03:49'),(2,4,'0X0000BA20',3.3,11.4,3999,74,7.2,36,1.7,28,43,51,'28-05-2020 09:03:49'),(2,5,'0X0000BA20',3.1,11.6,4089,676,7.1,46,1.7,19,48,48,'28-05-2020 09:03:49'),(2,6,'0X0000BA2F',3.3,13.7,3765,936,7,45,1.7,31,41,43,'28-05-2020 09:03:49'),(2,7,'0X0000BA2F',3.3,10.5,4129,619,6.8,45,1.3,28,46,40,'28-05-2020 09:03:49'),(2,8,'0X0000BA2F',3.6,13.6,4334,877,7.1,45,1.4,18,35,44,'28-05-2020 09:03:49'),(2,9,'0X0000BA2F',2.8,11.2,4125,378,6.9,43,1.1,23,45,44,'28-05-2020 09:03:49'),(2,10,'0X0000BA20',2.8,10.6,4036,839,7.2,37,1.2,23,43,51,'28-05-2020 09:03:49'),(3,1,'0X0000BA20',3.9,9.5,3966,47,7.2,45,1.1,30,43,46,'28-05-2020 09:03:49'),(3,2,'0X0000BA2F',2.9,13.4,4518,465,6.8,38,1.7,19,45,54,'28-05-2020 09:03:49'),(3,3,'0X0000BA2F',3.7,13.1,4499,856,6.9,39,1.6,27,44,35,'28-05-2020 09:03:49'),(3,4,'0X0000BA20',3.6,12,4424,458,6.8,45,1.4,27,47,51,'28-05-2020 09:03:49'),(3,5,'0X0000BA20',2.6,12.1,4314,961,7.1,39,1.3,26,38,49,'28-05-2020 09:03:49'),(3,6,'0X0000BA2F',2.8,13.3,3599,257,6.9,47,1.2,17,40,29,'28-05-2020 09:03:49'),(3,7,'0X0000BA2F',3.9,8.3,3853,879,7.1,41,1.4,37,39,31,'28-05-2020 09:03:49'),(3,8,'0X0000BA2F',3.1,8.7,4041,61,7.1,37,1.6,19,36,53,'28-05-2020 09:03:49'),(3,9,'0X0000BA20',2.7,10.2,4444,800,7.1,38,1,20,35,40,'28-05-2020 09:03:49'),(3,10,'0X0000BA2F',3.9,13.6,3951,418,7.1,40,1.6,31,36,28,'28-05-2020 09:03:49'),(4,1,'0X0000BA2F',3.9,12.7,3678,877,7.2,41,1.6,30,46,33,'28-05-2020 09:03:49'),(4,2,'0X0000BA2F',3.8,9.8,4572,520,6.9,41,1.4,31,41,29,'28-05-2020 09:03:49'),(4,3,'0X0000BA20',3.7,11.2,3922,226,6.9,41,1.5,35,46,46,'28-05-2020 09:03:49'),(4,4,'0X0000BA20',3.4,9.3,4463,111,7.1,42,1.3,28,44,54,'28-05-2020 09:03:49'),(4,5,'0X0000BA20',2.5,11,3515,803,7,41,1.4,25,41,42,'28-05-2020 09:03:49'),(4,6,'0X0000BA20',2.9,10.3,4509,595,6.9,41,1.6,32,48,38,'28-05-2020 09:03:49'),(4,7,'0X0000BA2F',3.1,12.3,4134,1025,7,39,1.6,21,39,50,'28-05-2020 09:03:49'),(4,8,'0X0000BA2F',2.6,13.5,4205,1013,6.8,35,1.3,32,43,47,'28-05-2020 09:03:49'),(4,9,'0X0000BA2F',3.2,12.7,4236,143,6.8,36,1.5,32,46,37,'28-05-2020 09:03:49'),(4,10,'0X0000BA2F',3.2,10.7,3554,323,6.8,47,1.5,28,39,30,'28-05-2020 09:03:49'),(5,1,'0X0000BA2F',3.7,8.4,3538,11,7.1,43,1.5,31,41,49,'28-05-2020 09:03:49'),(5,2,'0X0000BA20',2.9,13.5,4258,63,7.2,40,1.4,30,48,52,'28-05-2020 09:03:49'),(5,3,'0X0000BA2F',3.1,12.4,3805,786,6.9,35,1.5,28,40,44,'28-05-2020 09:03:49'),(5,4,'0X0000BA20',3.8,12.2,3718,146,7.2,42,1,26,45,30,'28-05-2020 09:03:49'),(5,5,'0X0000BA2F',3,9.4,4426,652,7,40,1.1,26,41,48,'28-05-2020 09:03:49'),(5,6,'0X0000BA20',3.5,12.8,3562,267,7.1,41,1.6,27,47,39,'28-05-2020 09:03:49'),(5,7,'0X0000BA20',3.4,8.4,4487,133,7,42,1.6,22,41,30,'28-05-2020 09:03:49'),(5,8,'0X0000BA2F',3.9,8.1,3602,654,7.1,35,1.1,26,37,48,'28-05-2020 09:03:49'),(5,9,'0X0000BA2F',3.9,9.3,3737,504,6.9,41,1.1,27,48,48,'28-05-2020 09:03:49'),(5,10,'0X0000BA20',4,10.3,4239,118,7.1,46,1.6,19,45,50,'28-05-2020 09:03:49'),(1,1,'0X0000BA2F',2.6,13.1,4106,341,7.1,45,1.5,26,47,45,'28-05-2020 09:04:33'),(1,2,'0X0000BA2F',3.5,8.4,3788,609,6.9,37,1.2,19,49,46,'28-05-2020 09:04:33'),(1,3,'0X0000BA2F',3.8,11.4,4357,449,7.2,40,1.6,29,40,32,'28-05-2020 09:04:33'),(1,4,'0X0000BA20',3.5,9.4,4267,438,7.1,36,1.5,20,41,37,'28-05-2020 09:04:33'),(1,5,'0X0000BA2F',3.7,12,4562,485,7.1,37,1.2,36,36,28,'28-05-2020 09:04:33'),(1,6,'0X0000BA20',3.3,9.3,3878,904,7.1,44,1.6,34,44,29,'28-05-2020 09:04:33'),(1,7,'0X0000BA2F',3.2,11.3,4392,556,6.9,37,1.3,35,37,36,'28-05-2020 09:04:33'),(1,8,'0X0000BA20',3.6,11.3,4310,771,6.9,35,1.4,23,39,49,'28-05-2020 09:04:33'),(1,9,'0X0000BA20',2.8,9.1,3861,271,7.2,35,1.3,25,41,34,'28-05-2020 09:04:33'),(1,10,'0X0000BA2F',3.3,9.2,3571,722,7,40,1.6,33,43,51,'28-05-2020 09:04:33'),(2,1,'0X0000BA2F',3.5,10.9,3931,963,6.8,43,1.6,34,36,51,'28-05-2020 09:04:33'),(2,2,'0X0000BA2F',4,13.4,4522,1033,7.1,43,1.6,23,49,38,'28-05-2020 09:04:33'),(2,3,'0X0000BA20',3,8.4,4352,147,7,41,1.1,23,45,42,'28-05-2020 09:04:33'),(2,4,'0X0000BA2F',2.7,9.9,4468,498,6.9,47,1.7,24,42,48,'28-05-2020 09:04:33'),(2,5,'0X0000BA2F',3.8,13.9,4356,690,7.1,41,1.6,27,35,44,'28-05-2020 09:04:33'),(2,6,'0X0000BA2F',4,9.3,3761,533,7.2,41,1.2,33,35,35,'28-05-2020 09:04:33'),(2,7,'0X0000BA20',3.6,11.3,3641,291,7,36,1.1,18,41,37,'28-05-2020 09:04:33'),(2,8,'0X0000BA20',2.6,10.1,3932,1010,7,41,1,25,42,28,'28-05-2020 09:04:33'),(2,9,'0X0000BA20',2.5,10.7,4151,938,7,41,1.5,17,45,34,'28-05-2020 09:04:33'),(2,10,'0X0000BA20',4,13.2,3969,59,6.9,42,1.3,33,37,33,'28-05-2020 09:04:33'),(3,1,'0X0000BA20',3.3,8.7,4321,672,6.9,45,1.3,21,35,44,'28-05-2020 09:04:33'),(3,2,'0X0000BA2F',3.5,9,3713,878,7.1,38,1.4,26,35,42,'28-05-2020 09:04:33'),(3,3,'0X0000BA2F',2.7,9,4383,413,6.9,46,1.2,28,43,41,'28-05-2020 09:04:33'),(3,4,'0X0000BA2F',3,13.4,4253,129,7,40,1.1,29,37,31,'28-05-2020 09:04:33'),(3,5,'0X0000BA2F',3.9,12.4,4271,230,7.1,35,1.4,21,35,46,'28-05-2020 09:04:33'),(3,6,'0X0000BA20',3.7,8.2,4510,910,6.9,37,1.5,18,36,34,'28-05-2020 09:04:33'),(3,7,'0X0000BA20',3.6,10.5,4449,721,6.8,40,1.2,24,35,29,'28-05-2020 09:04:33'),(3,8,'0X0000BA2F',3.9,11.7,4310,941,6.9,35,1.1,23,41,47,'28-05-2020 09:04:33'),(3,9,'0X0000BA2F',3.4,10.1,3944,269,7.2,38,1.6,18,41,34,'28-05-2020 09:04:33'),(3,10,'0X0000BA2F',3.7,12.9,3685,757,7,37,1,24,37,36,'28-05-2020 09:04:33'),(4,1,'0X0000BA20',3,9.1,3654,777,6.9,43,1.7,32,40,33,'28-05-2020 09:04:33'),(4,2,'0X0000BA20',2.8,13.1,4448,514,7,38,1.3,34,43,29,'28-05-2020 09:04:33'),(4,3,'0X0000BA2F',3.7,13.8,4097,628,7.2,47,1.6,33,37,33,'28-05-2020 09:04:33'),(4,4,'0X0000BA20',2.6,13,4324,354,7.2,41,1.5,21,47,30,'28-05-2020 09:04:33'),(4,5,'0X0000BA20',3.1,13.9,3824,470,7.1,37,1,32,46,38,'28-05-2020 09:04:33'),(4,6,'0X0000BA20',3.3,11.3,3743,819,6.9,38,1.5,36,39,32,'28-05-2020 09:04:33'),(4,7,'0X0000BA2F',3.3,9,3739,1013,7.1,46,1,23,45,45,'28-05-2020 09:04:33'),(4,8,'0X0000BA20',2.8,8.8,4327,656,6.9,44,1.1,27,45,39,'28-05-2020 09:04:33'),(4,9,'0X0000BA20',3.5,13.3,3763,68,6.9,38,1.2,37,46,46,'28-05-2020 09:04:33'),(4,10,'0X0000BA2F',4,13.8,3527,509,7.1,47,1.1,30,37,42,'28-05-2020 09:04:33'),(5,1,'0X0000BA2F',2.8,8.3,4569,218,7.2,40,1.6,32,35,52,'28-05-2020 09:04:33'),(5,2,'0X0000BA2F',2.6,9.5,4370,620,7,37,1.6,23,42,45,'28-05-2020 09:04:33'),(5,3,'0X0000BA20',2.8,10.6,4139,574,6.9,46,1.1,21,44,50,'28-05-2020 09:04:33'),(5,4,'0X0000BA20',3.8,14,3838,480,7.1,35,1.2,26,35,36,'28-05-2020 09:04:33'),(5,5,'0X0000BA20',3.8,13.2,3763,1039,7,37,1.5,37,46,36,'28-05-2020 09:04:33'),(5,6,'0X0000BA20',2.7,9.5,4365,360,7,46,1.3,29,36,38,'28-05-2020 09:04:33'),(5,7,'0X0000BA2F',3.2,8.1,4150,826,7.1,39,1.5,20,39,38,'28-05-2020 09:04:33'),(5,8,'0X0000BA2F',4,8.9,4466,406,7.2,40,1.5,29,37,45,'28-05-2020 09:04:33'),(5,9,'0X0000BA2F',2.5,13.5,4178,271,6.9,46,1.2,20,43,37,'28-05-2020 09:04:33'),(5,10,'0X0000BA20',3.2,10.7,3609,368,7.1,42,1.4,17,47,31,'28-05-2020 09:04:33');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-28  9:14:32