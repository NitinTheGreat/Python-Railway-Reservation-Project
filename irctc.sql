-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: irctc
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES ('a','a','a'),('akanksha','edsf','afyhhjjkk@gmail.com'),('alfred','prize','nobel@gmail'),('amy','ferrah','fowler@gmail'),('bhu','123','hgdjj@gmail'),('da','123','adadd'),('didi','sagarbrother','sister@sister.com'),('duo;wedoa','abc','ewohoie'),('fs','rf','fsfsf@gmail'),('geagaafdrgae','a','reafGe'),('gefa','afaf','sad'),('gefw','wfds','rfwds'),('george','georgie','george@gmail'),('hello','world','world@gmail'),('howard','astronaut','wolowitz@gmail'),('leonard','hofstader','leonard@gmail'),('mary','cooper','mary@gmail'),('missy','cooper','missy@gmail'),('new','123','new@gmail'),('NITIN','thegreat','nitin@gmail'),('nitin13','hello123','nitin@gmail'),('pranvi','1234','pranvi@gmai'),('Pratyush','pratyushlegend','pratyush@gmail'),('qw','dsa','dfs@gmail.com'),('raj','koothrapalli','rajesh@gmail'),('root','root','root@gmail'),('sheldon1','cooper','sheldon@nobel'),('shikha','123','shikha2@gmail'),('skd','fsfkm;fm','fslfn@gmail'),('trial20','123','trial@gmail'),('trial234','12','qwe@gmail'),('world','12','world@gmail'),('xyz123@12','gh','yzxdr@gmail'),('youtube','youtube','you@gmail');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail`
--

DROP TABLE IF EXISTS `detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detail` (
  `source` varchar(20) DEFAULT NULL,
  `destination` varchar(20) DEFAULT NULL,
  `distance` varchar(10) DEFAULT NULL,
  `traina` varchar(20) DEFAULT NULL,
  `trainb` varchar(20) DEFAULT NULL,
  `trainc` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail`
--

LOCK TABLES `detail` WRITE;
/*!40000 ALTER TABLE `detail` DISABLE KEYS */;
INSERT INTO `detail` VALUES ('DELHI','MUMBAI','3000','RAJDHANI EXPRESS','INTERCITY EXPRESS','SHATABDI EXPRESS'),('GORAKHPUR','LUCKNOW','1000','VAISHALI EXPRESS','INTERCITY EXPRESS','GORAKHDHAM EXPRESS'),('a','a','1000','bullet','train','super'),('GKP','DEL','1500','ABC','ABC','ABC'),('DELHI','LUCKNOW','1000','VAISHALI EXPRESS','GORAKHDHAM EXPRESS','RAJDHANI EXPRESS'),('GORAKHPUR','MUMBAI','3000','KUSHINAGAR EXPRESS','GKP LTT EXPRESS','BANDRA EXPRESS'),('MUMBAI','GORAKHPUR','3000','KUSHINAGAR EXPRESS','GKP LTT EXPRESS','BANDRA EXPRESS'),('LUCKNOW','DELHI','1000','VAISHALI EXPRESS','GORAKHDHAM EXPRESS','RAJDHANI EXPRESS'),('GORAKHPUR','DELHI','2000','VAISHALI EXPRESS','GORAKHDHAM EXPRESS','SAMPARK EXPRESS'),('DELHI','GORAKPUR','2000','VAISHALI EXPRESS','GORAKHDHAM EXPRESS','SAMPARK EXPRESS'),('DELHI','MUMBAI','1500','RAJDHANI EXPRESS','HUMSAFAR EXPRESS','TEJAS EXPRESS'),('MUMBAI','DELHI','1500','RAJDHANI EXPRESS','HUMSAFAR EXPRESS','TEJAS EXPRESS'),('GORAKHPUR','HYDERABAD','2500','GKP YELHANKA EXPRESS','GKP SC EXPRESS','GKP YPR EXPRESS'),('HYDERABAD','GORAKHPUR','2500','GKP YELHANKA EXPRESS','GKP SC EXPRESS','GKP YPR EXPRESS'),('GORAKHPUR','PATNA','700','PATLIPUTRA EXPRESS','VAISHALI EXPRESS','SAMPARK EXPRESS'),('PATNA','GORAKHPUR','700','PATLIPUTRA EXPRESS','VAISHALI EXPRESS','SAMPARK EXPRESS');
/*!40000 ALTER TABLE `detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mainpassenger`
--

DROP TABLE IF EXISTS `mainpassenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mainpassenger` (
  `name` varchar(20) DEFAULT NULL,
  `aadhar` varchar(15) NOT NULL,
  `AGE` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mainpassenger`
--

LOCK TABLES `mainpassenger` WRITE;
/*!40000 ALTER TABLE `mainpassenger` DISABLE KEYS */;
/*!40000 ALTER TABLE `mainpassenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger` (
  `name` varchar(20) DEFAULT NULL,
  `aadhar` varchar(15) NOT NULL,
  `AGE` varchar(3) DEFAULT NULL,
  `pnr` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`aadhar`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
INSERT INTO `passenger` VALUES ('trial 8','+65158653210','8','H92R51'),('dshkdbkja','12486541','4','H27R83'),('hello','1564646','40','D55241'),('gfds','23456u7','22','D91376'),('','24','','H24R24'),('trial1','243542424','23','D80318'),('TRIAL41','25889635','41','H41R87'),('russia','3543543','120','H17R42'),('','4234','','D60596'),('ukraine','456583265','500','D13922'),('gdheasjkl','456789','12','D68245'),('TRIAL333','45865789213','20','D16694'),('TRIAL20','46483q29','20','D88228'),('trial22','4872ruei','22','H94R48'),('kJASxm','532241','22','H64R82'),('','54','','D26659'),('','54321','','D40778'),('nitin','553113','20','D66966'),('trial 7','5643256321','7','D74556'),('NITIN','56895646','99','D76429'),('frewi','57834929','50','D32949'),('fresikd','65322e1','21','D92995'),('trial23','65384293','23','D54639'),('','6543','','H78R95'),('hellothere','65432','23','D78428'),('jkfdsl','654321','34@','D40868'),('trial4','654521','2','D62283'),('germany','65465312','105','H99R14'),('iehfjks','673289','69','D92589'),('ksjfda','67348290','69','H34R32'),('trial5','756321','3','H29R66'),('trial30','7632843298','30','D33345'),('trial6','76874521','6','D56915'),('munich','779859855','100','D58636'),('trial3','7845132','56','D37231'),('trial8','784653235','8','D88234'),('fhazds,','7856432','44','H51R92'),('fiwadsj','7865432','12','D11229'),('TRIAL444','78954689751','30','H61R27'),('11:22@gmail','7895545','22','D55381'),('trial8','7r2392120p','8','D82154'),('trial11','8+653235','45','D24266'),('djksnkl','848654','5','D79134'),('user1','854123165','500','D24218'),('oirewk','8573432','51','H64R86'),('fedsa','865312','78','D88357'),('HELLO WORLD','8746532785','100','D41137'),('trial40','875632','43','D93886'),('us','876545415','300','D57541'),('trial41','8765652','43','H61R97'),('6jhgfds','876u543','65','D40847'),('NOBEL','8785454554','700','H22R91'),('ksjd','89652','25','H64R91'),('TRIAL40','896532','40','D92332'),('gjefksl','896543','78','D68737'),('Pratyush Dubey','8976543','69','D17228'),('trial2','9+876561','56','D92588'),('trial12','965120','70','H18R17'),('trial15','978653','45','D89883'),('FGEDSJ','978765567','985','D11621'),('dadd','dada','dad','H81R28'),('ad','ddwedd','da','D52555'),('trial21','yirk3492','21','D74437');
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `source` varchar(20) NOT NULL,
  `destination` varchar(20) DEFAULT NULL,
  `distance` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`source`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES ('DELHI','MUMBAI','3000');
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-06 17:32:33
