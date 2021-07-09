-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: bingeParty
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

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
-- Table structure for table `Cameron`
--

DROP TABLE IF EXISTS `Cameron`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cameron` (
  `ID` text DEFAULT NULL,
  `Type` text DEFAULT NULL,
  `Title` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cameron`
--

LOCK TABLES `Cameron` WRITE;
/*!40000 ALTER TABLE `Cameron` DISABLE KEYS */;
INSERT INTO `Cameron` VALUES ('615658','movie','Awake');
/*!40000 ALTER TABLE `Cameron` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cleo`
--

DROP TABLE IF EXISTS `Cleo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cleo` (
  `ID` text DEFAULT NULL,
  `Type` text DEFAULT NULL,
  `Title` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cleo`
--

LOCK TABLES `Cleo` WRITE;
/*!40000 ALTER TABLE `Cleo` DISABLE KEYS */;
INSERT INTO `Cleo` VALUES ('1447','tv','Psych'),('57243','tv','Doctor Who'),('716258','movie','Black Box'),('405774','movie','Bird Box'),('1418','tv','The Big Bang Theory');
/*!40000 ALTER TABLE `Cleo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jane`
--

DROP TABLE IF EXISTS `Jane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Jane` (
  `ID` text DEFAULT NULL,
  `Type` text DEFAULT NULL,
  `Title` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jane`
--

LOCK TABLES `Jane` WRITE;
/*!40000 ALTER TABLE `Jane` DISABLE KEYS */;
INSERT INTO `Jane` VALUES ('497698','movie','Black Widow'),('84958','tv','Loki'),('299534','movie','Avengers: Endgame');
/*!40000 ALTER TABLE `Jane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jason`
--

DROP TABLE IF EXISTS `Jason`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Jason` (
  `ID` text DEFAULT NULL,
  `Type` text DEFAULT NULL,
  `Title` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jason`
--

LOCK TABLES `Jason` WRITE;
/*!40000 ALTER TABLE `Jason` DISABLE KEYS */;
INSERT INTO `Jason` VALUES ('246655','movie','X-Men: Apocalypse');
/*!40000 ALTER TABLE `Jason` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-09 18:20:55
