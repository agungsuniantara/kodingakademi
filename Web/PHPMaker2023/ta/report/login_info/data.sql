/*
SQLyog Ultimate v10.42 
MySQL - 5.5.27 : Database - epiz_22636514_ponpes
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`epiz_22636514_ponpes` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `epiz_22636514_ponpes`;

/*Table structure for table `d_biaya` */

DROP TABLE IF EXISTS `d_biaya`;

CREATE TABLE `d_biaya` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code_grp_bya` varchar(5) DEFAULT NULL,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `d_biaya` */

insert  into `d_biaya`(`code_auto`,`code_grp_bya`,`code`,`nama`,`active`) values (1,'GBY01','B0001','GAJI GURU',1),(2,'GBY01','B0002','GAJI PEGAWAI',1),(3,'GBY01','B0003','KONSUMSI HARIAN',1),(4,'GBY01','B0004','TUNJANGAN2',1),(5,'GBY01','B0005','PERAWATAN GADUNG DAN LINGKUNGAN',1),(6,'GBY01','B0006','PENGEMBANGAN FISIK',1),(7,'GBY01','B0007','PENGEMBANGAN NON FISIK',1),(8,'GBY01','B0008','KOPERASI PONPES',1);

/*Table structure for table `d_djenis_laporan_bya` */

DROP TABLE IF EXISTS `d_djenis_laporan_bya`;

CREATE TABLE `d_djenis_laporan_bya` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code_jlp` varchar(5) DEFAULT NULL,
  `code_grp` varchar(5) DEFAULT NULL,
  `code_bya` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `d_djenis_laporan_bya` */

insert  into `d_djenis_laporan_bya`(`code_auto`,`code_jlp`,`code_grp`,`code_bya`) values (1,'JLP01','GBY01','B0001'),(2,'JLP01','GBY01','B0002'),(3,'JLP01','GBY01','B0003'),(4,'JLP01','GBY01','B0004'),(5,'JLP01','GBY01','B0005'),(6,'JLP01','GBY01','B0006'),(7,'JLP01','GBY01','B0007'),(8,'JLP01','GBY01','B0008'),(9,'JLP02','GBY01','B0008');

/*Table structure for table `d_djenis_laporan_pdp` */

DROP TABLE IF EXISTS `d_djenis_laporan_pdp`;

CREATE TABLE `d_djenis_laporan_pdp` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code_jlp` varchar(5) DEFAULT NULL,
  `code_grp` varchar(5) DEFAULT NULL,
  `code_pdp` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `d_djenis_laporan_pdp` */

insert  into `d_djenis_laporan_pdp`(`code_auto`,`code_jlp`,`code_grp`,`code_pdp`) values (1,'JLP01','GPD01','P0004'),(2,'JLP01','GPD02','P0003'),(3,'JLP01','GPD03','P0005'),(4,'JLP01','GPD04','P0001'),(5,'JLP01','GPD05','P0002'),(6,'JLP01','GPD06','P0006'),(7,'JLP01','GPD06','P0007'),(8,'JLP01','GPD06','P0008'),(9,'JLP01','GPD06','P0009'),(10,'JLP01','GPD06','P0010'),(11,'JLP01','GPD06','P0011'),(12,'JLP02','GPD06','P0010');

/*Table structure for table `d_group_biaya` */

DROP TABLE IF EXISTS `d_group_biaya`;

CREATE TABLE `d_group_biaya` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `d_group_biaya` */

insert  into `d_group_biaya`(`code_auto`,`code`,`nama`,`active`) values (1,'GBY01','BIAYA',1);

/*Table structure for table `d_group_kas_bank` */

DROP TABLE IF EXISTS `d_group_kas_bank`;

CREATE TABLE `d_group_kas_bank` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `d_group_kas_bank` */

insert  into `d_group_kas_bank`(`code_auto`,`code`,`nama`,`active`) values (1,'GKB01','KAS',1),(2,'GKB02','BANK',1);

/*Table structure for table `d_group_pendapatan` */

DROP TABLE IF EXISTS `d_group_pendapatan`;

CREATE TABLE `d_group_pendapatan` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `d_group_pendapatan` */

insert  into `d_group_pendapatan`(`code_auto`,`code`,`nama`,`active`) values (1,'GPD01','MTS',1),(2,'GPD02','MA',1),(3,'GPD03','SMK',1),(4,'GPD04','ASRAMA PUTRA',1),(5,'GPD05','ASRAMA PUTRI',1),(6,'GPD06','INSIDENTIL/UMUM',1);

/*Table structure for table `d_jabatan` */

DROP TABLE IF EXISTS `d_jabatan`;

CREATE TABLE `d_jabatan` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `d_jabatan` */

insert  into `d_jabatan`(`code_auto`,`code`,`nama`,`active`) values (1,'JAB01','DIREKTUR',1),(2,'JAB02','KABAG KUANGAN & ADMIN',1),(3,'JAB03','BENDAHARA',1);

/*Table structure for table `d_jenis_laporan` */

DROP TABLE IF EXISTS `d_jenis_laporan`;

CREATE TABLE `d_jenis_laporan` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `d_jenis_laporan` */

insert  into `d_jenis_laporan`(`code_auto`,`code`,`nama`,`active`) values (1,'JLP01','LAPORAN LABA/RUGI (UMUM)',1),(2,'JLP02','LABA/RUGI (KOPERASI)',1);

/*Table structure for table `d_kas_bank` */

DROP TABLE IF EXISTS `d_kas_bank`;

CREATE TABLE `d_kas_bank` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code_grp_kbn` varchar(5) DEFAULT NULL,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `d_kas_bank` */

insert  into `d_kas_bank`(`code_auto`,`code_grp_kbn`,`code`,`nama`,`active`) values (1,'GKB01','KBN01','KAS KECIL',1),(2,'GKB01','KBN02','KAS BESAR',1),(3,'GKB02','KBN03','BANK BRI (ACC : 5430030030003)',1);

/*Table structure for table `d_login` */

DROP TABLE IF EXISTS `d_login`;

CREATE TABLE `d_login` (
  `code_auto` int(10) NOT NULL AUTO_INCREMENT,
  `user_level` tinyint(1) DEFAULT NULL,
  `code` varchar(5) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `code_jab` varchar(5) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `user_pass` varchar(254) DEFAULT NULL,
  `acs_01` enum('1') DEFAULT NULL,
  `acs_02` enum('1') DEFAULT NULL,
  `acs_03` enum('1') DEFAULT NULL,
  `acs_04` enum('1') DEFAULT NULL,
  `acs_05` enum('1') DEFAULT NULL,
  `acs_06` enum('1') DEFAULT NULL,
  `acs_07` enum('1') DEFAULT NULL,
  `acs_08` enum('1') DEFAULT NULL,
  `acs_09` enum('1') DEFAULT NULL,
  `acs_10` enum('1') DEFAULT NULL,
  `acs_11` enum('1') DEFAULT NULL,
  `acs_12` enum('1') DEFAULT NULL,
  `acs_13` enum('1') DEFAULT NULL,
  `acs_14` enum('1') DEFAULT NULL,
  `acs_15` enum('1') DEFAULT NULL,
  `acs_16` enum('1') DEFAULT NULL,
  `acs_17` enum('1') DEFAULT NULL,
  `pict_signature` blob,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `d_login` */

insert  into `d_login`(`code_auto`,`user_level`,`code`,`name`,`code_jab`,`user_email`,`user_name`,`user_pass`,`acs_01`,`acs_02`,`acs_03`,`acs_04`,`acs_05`,`acs_06`,`acs_07`,`acs_08`,`acs_09`,`acs_10`,`acs_11`,`acs_12`,`acs_13`,`acs_14`,`acs_15`,`acs_16`,`acs_17`,`pict_signature`) values (1,-1,'LGN01','Admin','JAB01','admin@admin.com','admin','827ccb0eea8a706c4c34a16891f84e7b','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',NULL);

/*Table structure for table `d_pendapatan` */

DROP TABLE IF EXISTS `d_pendapatan`;

CREATE TABLE `d_pendapatan` (
  `code_auto` int(5) NOT NULL AUTO_INCREMENT,
  `code_grp_pdp` varchar(5) DEFAULT NULL,
  `code` varchar(5) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `d_pendapatan` */

insert  into `d_pendapatan`(`code_auto`,`code_grp_pdp`,`code`,`nama`,`active`) values (1,'GPD04','P0001','ASRAMA PUTRA',1),(2,'GPD05','P0002','ASRAMA PUTRI',1),(3,'GPD02','P0003','MA',1),(4,'GPD01','P0004','MTS',1),(5,'GPD03','P0005','SMK',1),(6,'GPD06','P0006','SUMBANGAN PEMERINTAH',1),(7,'GPD06','P0007','LEMBAGA',1),(8,'GPD06','P0008','INDIVIDU',1),(9,'GPD06','P0009','KAI',1),(10,'GPD06','P0010','KOPERASI PONPES',1),(11,'GPD06','P0011','WALI SANTRI',1);

/*Table structure for table `t_kas_keluar` */

DROP TABLE IF EXISTS `t_kas_keluar`;

CREATE TABLE `t_kas_keluar` (
  `code_auto` int(10) NOT NULL AUTO_INCREMENT,
  `tanggal` date DEFAULT NULL,
  `no_bukti` varchar(15) DEFAULT NULL,
  `code_kbn` varchar(5) DEFAULT NULL,
  `tmp_nm_kbn` varchar(50) DEFAULT NULL,
  `keterangan` text,
  `jumlah` int(10) DEFAULT NULL,
  `code_grp_bya` varchar(5) DEFAULT NULL,
  `tmp_nm_grp_bya` varchar(50) DEFAULT NULL,
  `code_bya` varchar(5) DEFAULT NULL,
  `tmp_nm_bya` varchar(50) DEFAULT NULL,
  `file_01` blob,
  `file_02` blob,
  `file_03` blob,
  `code_usr_crt` varchar(5) DEFAULT NULL,
  `tmp_nmu_usr_crt` varchar(50) DEFAULT NULL,
  `tgl_crt` datetime DEFAULT NULL,
  `code_usr_upd` varchar(5) DEFAULT NULL,
  `tmp_nmu_usr_upd` varchar(50) DEFAULT NULL,
  `tgl_upd` datetime DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `t_kas_keluar` */

/*Table structure for table `t_kas_masuk` */

DROP TABLE IF EXISTS `t_kas_masuk`;

CREATE TABLE `t_kas_masuk` (
  `code_auto` int(10) NOT NULL AUTO_INCREMENT,
  `tanggal` date DEFAULT NULL,
  `no_bukti` varchar(15) DEFAULT NULL,
  `code_kbn` varchar(5) DEFAULT NULL,
  `tmp_nm_kbn` varchar(50) DEFAULT NULL,
  `keterangan` text,
  `jumlah` int(10) DEFAULT NULL,
  `code_grp_pdp` varchar(5) DEFAULT NULL,
  `tmp_nm_grp_pdp` varchar(50) DEFAULT NULL,
  `code_pdp` varchar(5) DEFAULT NULL,
  `tmp_nm_pdp` varchar(50) DEFAULT NULL,
  `file_01` blob,
  `file_02` blob,
  `file_03` blob,
  `code_usr_crt` varchar(5) DEFAULT NULL,
  `tmp_nmu_usr_crt` varchar(50) DEFAULT NULL,
  `tgl_crt` datetime DEFAULT NULL,
  `code_usr_upd` varchar(5) DEFAULT NULL,
  `tmp_nmu_usr_upd` varchar(50) DEFAULT NULL,
  `tgl_upd` datetime DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `t_kas_masuk` */

insert  into `t_kas_masuk`(`code_auto`,`tanggal`,`no_bukti`,`code_kbn`,`tmp_nm_kbn`,`keterangan`,`jumlah`,`code_grp_pdp`,`tmp_nm_grp_pdp`,`code_pdp`,`tmp_nm_pdp`,`file_01`,`file_02`,`file_03`,`code_usr_crt`,`tmp_nmu_usr_crt`,`tgl_crt`,`code_usr_upd`,`tmp_nmu_usr_upd`,`tgl_upd`) values (1,'2018-09-07','BKM0000000001','KBN02','KAS BESAR','keterangan',1000000,'GPD02','MA','P0003','MA',NULL,NULL,NULL,'','','2018-09-07 06:25:49',NULL,NULL,NULL);

/*Table structure for table `t_kas_trf` */

DROP TABLE IF EXISTS `t_kas_trf`;

CREATE TABLE `t_kas_trf` (
  `code_auto` int(10) NOT NULL AUTO_INCREMENT,
  `tanggal` date DEFAULT NULL,
  `no_bukti` varchar(15) DEFAULT NULL,
  `code_kbn_dari` varchar(5) DEFAULT NULL,
  `tmp_nm_kbn_dari` varchar(50) DEFAULT NULL,
  `keterangan` text,
  `jumlah` int(10) DEFAULT NULL,
  `code_kbn_ke` varchar(5) DEFAULT NULL,
  `tmp_nm_kbn_ke` varchar(50) DEFAULT NULL,
  `file_01` blob,
  `file_02` blob,
  `file_03` blob,
  `code_usr_crt` varchar(5) DEFAULT NULL,
  `tmp_nmu_usr_crt` varchar(50) DEFAULT NULL,
  `tgl_crt` datetime DEFAULT NULL,
  `code_usr_upd` varchar(5) DEFAULT NULL,
  `tmp_nmu_usr_upd` varchar(50) DEFAULT NULL,
  `tgl_upd` datetime DEFAULT NULL,
  PRIMARY KEY (`code_auto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `t_kas_trf` */

insert  into `t_kas_trf`(`code_auto`,`tanggal`,`no_bukti`,`code_kbn_dari`,`tmp_nm_kbn_dari`,`keterangan`,`jumlah`,`code_kbn_ke`,`tmp_nm_kbn_ke`,`file_01`,`file_02`,`file_03`,`code_usr_crt`,`tmp_nmu_usr_crt`,`tgl_crt`,`code_usr_upd`,`tmp_nmu_usr_upd`,`tgl_upd`) values (1,'2018-09-01','BKT0000000001','KBN01','KAS KECIL','transfer 123',100000,'KBN01','KAS KECIL',NULL,NULL,NULL,'','','2018-09-29 06:38:02',NULL,NULL,NULL),(2,'2018-09-30','BKT0000000002','KBN02','KAS BESAR','xddfdf',20000,'KBN01','KAS KECIL',NULL,NULL,NULL,'','','2018-09-30 16:35:00',NULL,NULL,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
