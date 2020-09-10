-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Dev: @GorpoOrko
-- Site: httpd://tcxsproject.com.br
-- Github: https://github.com/gorpo
-- Este dump faz parte do sistema para PlayStation3 da TCXS Project Web Store PHP Mysql
-- Versão do servidor: 10.4.6-MariaDB
-- versão do PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `tcxs_store`
--

-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_users`
--

CREATE TABLE `playstation_users` (
  `id` mediumint(9) NOT NULL,
  `usuario` varchar(200) NOT NULL,
  `senha` varchar(329) NOT NULL,
  `nome` varchar(999) NOT NULL,
  `cadastro` datetime NOT NULL,
  `nivel` varchar(999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `playstation_users`
--

INSERT INTO `playstation_users` (`id`, `usuario`, `senha`, `nome`, `cadastro`, `nivel`) VALUES
('3','gorpo','gorpo','Gorpo','2500-01-11 19:42:12','admin'),
('4','gorp','corp','Gorpo','2500-01-11 19:42:12','admin'),
('5','gorpo','corpo','Gorpo','2500-01-11 19:42:12','admin'),
('6','mitsuki','tcxsproject2020web','Mitsuki','2500-09-07 15:06:19','admin'),
('7','mit','mit','Mitsuki','2500-09-07 15:06:25','admin'),
('8','ted','ted','MsTe3dz','2500-09-07 15:06:25','admin');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_infos`
--

CREATE TABLE `playstation_infos` (
  `id` mediumint(9) NOT NULL,
  `informacao` varchar(999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `playstation_infos`
--

INSERT INTO `playstation_infos` (`id`, `informacao`) VALUES
('3','XASDASD'),
('4','XASDASD'),
('5','XASDASD'),
('6','XASDASD');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_psp`
--

CREATE TABLE `playstation_psp` (
  `id` int(255) NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_psp`
--

INSERT INTO `playstation_psp` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES
('3','Air Conflicts Aces of World War 2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10404_00-0000000000000001','airconflicts2.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/8ykm4hlzxf985hk/PSPPS3-ULUS10404_00-0000000000000001.pkg?dl=1'),
('4','Armored Core Formula Front','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULJS00003_00-0000000000000001','armoredcoreformula.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/j5r9n7sq7dsiulu/PSPPS3-ULJS00003_00-0000000000000001.pkg?dl=1'),
('5','Astonishia Story','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10083_00-0000000000000001','astonishia.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/umn45hsdkp8cdv6/PSPPS3-ULUS10083_00-0000000000000001.pkg?dl=1'),
('6','Beats','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-NPEG00001_00-0000000000000001','beats.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/9b4n9njyhe4g9t6/PSPPS3-NPEG00001_00-0000000000000001.pkg?dl=1'),
('7','Ben 10 Alien Force','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10387_00-0000000000000001','benalien.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/abpzpsmy2lffqr2/PSPPS3-ULUS10387_00-0000000000000001.pkg?dl=1'),
('8','Blade Dancer Lineage of Light','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10124_00-0000000000000001','bladedancer.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/8td4rakag7tl0zz/PSPPS3-ULUS10124_00-0000000000000001.pkg?dl=1'),
('9','Catlevania Dracula X Chronicles','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10277_00-0000000000000001','castlevaniadraculaxchronicles.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/1vl6v9pq5iqnmgx/PSPPS3-ULUS10277_00-0000000000000001.pkg?dl=1'),
('10','Class of Heroes','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10396_00-0000000000000001','classofheroes.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/i1dmmrytwrb0ncl/PSPPS3-ULUS10396_00-0000000000000001.pkg?dl=1'),
('11','Crash','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10377_00-0000000000000001','crashmom.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/g3fh3md6cvfb1hd/PSPPS3-ULUS10377_00-0000000000000001.pkg?dl=1'),
('12','Dead Head Fred','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10495_00-0000000000000001','deadheadfred.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/zjh68al7q5t15x2/PSPPS3-ULUS10495_00-0000000000000001.pkg?dl=1'),
('13','Exit 2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','FALTA CONTENT_ID','exit2.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/link_do_jogo.pkg?dl=1'),
('14','Fading Shadows','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES00285_00-0000000000000001','fadings.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/c0fde57apeqskme/PSPPS3-ULES00285_00-0000000000000001.pkg?dl=1'),
('15','Final Fantasy Dissidia','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10437_00-0000000000000001','ffdissidia.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/hic90fyynvkkmmk/PSPPS3-ULUS10437_00-0000000000000001.pkg?dl=1'),
('16','Final Fantasy VII Crisis Core','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES00285_00-0000000000000001','ffcrisiscore.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/c0fde57apeqskme/PSPPS3-ULES00285_00-0000000000000001.pkg?dl=1'),
('17','Formula 1 2009','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES01355_00-0000000000000001','f12009.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/lenuson5qaqr8dc/PSPPS3-ULES01355_00-0000000000000001.pkg?dl=1'),
('18','Hellboy The Science of Evil','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES00827_00-0000000000000001','hellboythescience.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/nwoyfxwlpzzosm2/PSPPS3-ULES00827_00-0000000000000001.pkg?dl=1'),
('19','Jeanne DArc','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES01355_00-0000000000000001','jeannedarc.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/lenuson5qaqr8dc/PSPPS3-ULES01355_00-0000000000000001.pkg?dl=1'),
('20','La Pucelle Ragnarok','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULJS00244_00-0000000000000001','lapucelleragnarok.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/pdhlb8p4nrqkibq/PSPPS3-ULJS00244_00-0000000000000001.pkg?dl=1'),
('21','Lunar Silver Star Harmony','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10482_00-0000000000000001','lunar.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/oky9bxyz84itana/PSPPS3-ULUS10482_00-0000000000000001.pkg?dl=1'),
('22','Mega Man Maverick Hunter X','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10068_00-0000000000000001','megamanmx.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/vntc0zivq6momuj/PSPPS3-ULUS10068_00-0000000000000001.pkg?dl=1'),
('23','Metal Gear Ac!d 1','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10006_00-0000000000000001','mgsacid.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/lip0l0ceidqb36y/PSPPS3-ULUS10006_00-0000000000000001.pkg?dl=1'),
('24','Metal Slug XX','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10495_00-0000000000000001','metalslugxx.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/ymsrnlwg4aokkew/PSPPS3-ULUS10495_00-0000000000000001.pkg?dl=1'),
('25','Prinny 1 Can I Really Be a Hero?','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10407_00-0000000000000001','prinny1.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/hud7vusn8pnatrf/PSPPS3-ULUS10407_00-0000000000000001.pkg?dl=1'),
('26','Prinny 2 Dawn of Operation Panties, Dood!','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10561_00-0000000000000001','prinny2.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/c5j55j8cx66u5eu/PSPPS3-ULUS10561_00-0000000000000001.pkg?dl=1'),
('27','Silent Hill Origins','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10285_00-0000000000000001','silenthillorigins.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/qouzncuofpup7j2/PSPPS3-ULUS10285_00-0000000000000001.pkg?dl=1'),
('28','Soul Calibur Broken Destiny','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES01298_00-0000000000000001','soulcaliburbrokendestiny.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/tsycqnmmj9piak0/PSPPS3-ULES01298_00-0000000000000001.pkg?dl=1'),
('29','Soul Eater Battle Resonance','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULJS00176_00-0000000000000001','souleater.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/7xykmok2d5i58nn/PSPPS3-ULJS00176_00-0000000000000001.pkg?dl=1'),
('30','Spider Man 2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES00022_00-0000000000000001','spiderman2.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/3qhhzq7ohgjvci2/PSPPS3-ULES00022_00-0000000000000001.pkg?dl=1'),
('31','Star Wars Battlefront 2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES00183_00-0000000000000001','starwarsbattlefront2.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/ygyeic91sd7oc3p/PSPPS3-ULES00183_00-0000000000000001.pkg?dl=1'),
('32','Strikers 1945 Plus','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULKS46198_00-0000000000000001','strikers1945plus.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/nicbev3w69av7r4/PSPPS3-ULKS46198_00-0000000000000001.pkg?dl=1'),
('33','Super Pocket Tennis','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES00619_00-0000000000000001','superpt.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/tj7rzrb9saeduoc/PSPPS3-ULES00619_00-0000000000000001.pkg?dl=1'),
('34','The 3rd Birthday','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','FALTA CONTENT_ID','the3rd.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/link_do_jogo.pkg?dl=1'),
('35','Valhalla Kinights 2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULUS10366_00-0000000000000001','valhallaknights2.jpg','2020-09-02 15:26:40','https://www.dropbox.com/s/1e73gscd5x8q6fm/PSPPS3-ULUS10366_00-0000000000000001.pkg?dl=1'),
('36','WallDDDDDDDD','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PSP','PSPPS3-ULES01072_00-0000000000000001','walle.jpg','2020-09-02 20:47:14','https://www.dropbox.com/s/jna5djyhe7u2m8l/PSPPS3-ULES01072_00-0000000000000001.pkg?dl=1');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_ps1`
--

CREATE TABLE `playstation_ps1` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_ps1`
--

INSERT INTO `playstation_ps1` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES
('3','1Xtreme','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94503_00-0000000000000001','1xtreme.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/rciydbdh5l7bvya/UP9000-SCUS94503_00-0000000000000001.pkg?dl=1'),
('4','3Xtreme','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94231_00-0000000000000001','3xtreme.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ib8157pwvirgqjh/UP9000-SCUS94231_00-0000000000000001.pkg?dl=1'),
('5','Ace Combat 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00404_00-0000000000000001','acecombat2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ptjalqzvcbns075/UP9000-SLUS00404_00-0000000000000001.pkg?dl=1'),
('6','Adventures of Lomax','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94906_00-0000000000000001','lomax.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/x6gsn7ll1sx0ndr/UP9000-SCUS94906_00-0000000000000001.pkg?dl=1'),
('7','Aladdin  La Venganza de Nasira','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCES03008_00-0000000000000001','aladdin.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/5wnhbwcosy5m1rq/UP9000-SCES03008_00-0000000000000001.pkg?dl=1'),
('8','Alien Trilog','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00007_00-0000000000000001','alientrilogy.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/erkpjbktj4geijl/UP9000-SLUS00007_00-0000000000000001.pkg?dl=1'),
('9','Alone in the Dark CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01201_00-0000000000000001','alone.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6dhjjp0o0w9qwpn/UP9000-SLUS01201_00-0000000000000001.pkg?dl=1'),
('10','Alone in the Dark CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01201_00-0000000000000001','alone.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0isugqcd7f7a1v9/UP9000-SLUS01201_00-0000000000000001.pkg?dl=1'),
('11','Alundra','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00553_00-0000000000000001','alundra.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/r02ysa4ulc9vx52/UP9000-SLUS00553_00-0000000000000001.pkg?dl=1'),
('12','Amerzone  O Testamento do Explorador CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00553_00-0000000000000001','amerzone.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/r02ysa4ulc9vx52/UP9000-SLUS00553_00-0000000000000001.pkg?dl=1'),
('13','Amerzone  O Testamento do Explorador CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES12429_00-0000000000000001','amerzone.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/rzjihxypo9z0k2p/UP9000-SLES12429_00-0000000000000001.pkg?dl=1'),
('14','Ape Scape','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94423_00-0000000000000001%20-%20Ape','apescape.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/zq33zewbpoyri92/UP9000-SCUS94423_00-0000000000000001%20-%20Ape.pkg?dl=1'),
('15','Apocalypse','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00373_00-0000000000000001','apocalypse.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ve7o0wdiqkdv6ix/UP9000-SLUS00373_00-0000000000000001.pkg?dl=1'),
('16','Asterix','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES01748_00-0000000000000001','asterix.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/g7ipy5aib08cnvs/UP9000-SLES01748_00-0000000000000001.pkg?dl=1'),
('17','Asteroids','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00773_00-0000000000000001','asteroids.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/p7whpkbfch7j173/UP9000-SLUS00773_00-0000000000000001.pkg?dl=1'),
('18','Atlantis - The Lost Empire','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCES03543_00-0000000000000001','atlantis.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/yqf5u61k0ypffd0/UP9000-SCES03543_00-0000000000000001.pkg?dl=1'),
('19','Attack of the Saucerman','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01718_00-0000000000000001','attackofthesaucerman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/m0i7co2x76bozwj/UP9000-SLUS01718_00-0000000000000001.pkg?dl=1'),
('20','Battle Arena Toshinden','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94200_00-0000000000000001','battlearenatoshinden.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/mjlc06ltpwlg736/UP9000-SCUS94200_00-0000000000000001.pkg?dl=1'),
('21','Battle Arena Toshinden 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00220_00-0000000000000001','battlearenatoshinden2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/gl0q21bo7769l6b/UP9000-SLUS00220_00-0000000000000001.pkg?dl=1'),
('22','Battle Arena Toshiden 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00483_00-0000000000000001','battlearenatoshinden3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/v18unqcd3towqtg/UP9000-SLUS00483_00-0000000000000001.pkg?dl=1'),
('23','Beyblade','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01489_00-0000000000000001','beyblade.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/suzxodu9j4p7nrn/UP9000-SLUS01489_00-0000000000000001.pkg?dl=1'),
('24','Bloody Roar','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94199_00-0000000000000001','bloodyroar1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/w4zg9jhcqlkjd37/UP9000-SCUS94199_00-0000000000000001.pkg?dl=1'),
('25','Bloody Roar 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94424_00-0000000000000001','bloodyroar2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ug7k41uq9mdfp6a/UP9000-SCUS94424_00-0000000000000001.pkg?dl=1'),
('26','BomberMan Party','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01189_00-0000000000000001','bombermanp.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/awzleveedjsykio/UP9000-SLUS01189_00-0000000000000001.pkg?dl=1'),
('27','Bomberman Fantasy Race','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00823_00-0000000000000001','bomberrace.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/pdcjrzjbf35x9of/UP9000-SLUS00823_00-0000000000000001.pkg?dl=1'),
('28','Bomberman World','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00680_00-0000000000000001','bomberworld.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/vz49j71irfdum1q/UP9000-SLUS00680_00-0000000000000001.pkg?dl=1'),
('29','Breath of fire 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00422_00-0000000000000001','breath3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/35q024etak1vkhq/UP9000-SLUS00422_00-0000000000000001.pkg?dl=1'),
('30','Breath of fire 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01324_00-0000000000000001','breathoffire4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/4phjl6qyjsuz93h/UP9000-SLUS01324_00-0000000000000001.pkg?dl=1'),
('31','A Bugs Life','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94288_00-0000000000000001','bugslife.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/dxt415c3ha5oequ/UP9000-SCUS94288_00-0000000000000001.pkg?dl=1'),
('32','Bugs Bunny &amp; Taz  Time Busters','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01144_00-0000000000000001','bugstime.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0hbfumesji6l06j/UP9000-SLUS01144_00-0000000000000001.pkg?dl=1'),
('33','Busta Groove','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94263_00-0000000000000001','bustagroove.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7esvajs7x0bakvs/UP9000-SCUS94263_00-0000000000000001.pkg?dl=01'),
('34','Busta Groove 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01159_00-0000000000000001','bustagroove2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/izxgp89e1cfx0w2/UP9000-SLUS01159_00-0000000000000001.pkg?dl=1'),
('35','Castlevania Simphony of Night','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00067_00-0000000000000001','castlevaniasimphony.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/tcn2681rbyt9o1z/UP9000-SLUS00067_00-0000000000000001.pkg?dl=1'),
('36','Castlevania Chronicles','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01384_00-0000000000000001','castlevaniasimphony.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7szm2x9gilqnwnt/UP9000-SLUS01384_00-0000000000000001.pkg?dl=1'),
('37','Chrono Cross CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01041_00-0000000000000001','chronocross.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/uwyneniae2lj97g/UP9000-SLUS01041_00-0000000000000001.pkg?dl=1'),
('38','Chrono Cross CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01041_00-0000000000000001','chronocross.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/5n7dn4jxyt5lo0z/UP9000-SLUS01041_00-0000000000000001.pkg?dl=1'),
('39','Clock Tower','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00539_00-0000000000000001','clocktower.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/k6lsvbg1jjd1y0j/UP9000-SLUS00539_00-0000000000000001.pkg?dl=1'),
('40','Clock Tower 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00695_00-0000000000000001','clocktower2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/mo9wf815gic03oi/UP9000-SLUS00695_00-0000000000000001.pkg?dl=1'),
('41','Contra Legacy War','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00288_00-0000000000000001','contrawar.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qieg3xkprzu80re/UP9000-SLUS00288_00-0000000000000001.pkg?dl=1'),
('42','Courier Crisis','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00442_00-0000000000000001','courier.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/5df3cvhshxr8hmf/UP9000-SLUS00442_00-0000000000000001.pkg?dl=1'),
('43','Crash Bandicoot','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS94900_00-0000000000000001','crash1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ekbfyu2rv47zzdq/UP9000-SLUS94900_00-0000000000000001.pkg?dl=1'),
('44','Crash Bandicoot 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94154_00-0000000000000001','crash2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/cyyeyuuxrhoncdp/UP9000-SCUS94154_00-0000000000000001.pkg?dl=1'),
('45','Crash Bandicoot 3 Warped','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94244_00-0000000000000001','crash3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/9acaxhfa9x0wv0x/UP9000-SCUS94244_00-0000000000000001.pkg?dl=1'),
('46','Crime Killer','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00576_00-0000000000000001','crimekiller.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/hngur5fzee5fdru/UP9000-SLUS00576_00-0000000000000001.pkg?dl=1'),
('47','Crash Team Racing','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94426_00-0000000000000001','ctr.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fa1tdp77pynyqe6/UP9000-SCUS94426_00-0000000000000001.pkg?dl=1'),
('48','DragonBall Final Bout','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLPS00949_00-0000000000000001','dbztrilgy.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ypyo9os1kxzg70a/UP9000-SLPS00949_00-0000000000000001.pkg?dl=1'),
('49','Diablo','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00619_00-0000000000000001','diablo.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/2lnaflzi1u14r3j/UP9000-SLUS00619_00-0000000000000001.pkg?dl=1'),
('50','Digimon Rumble Arena','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01404_00-0000000000000001','digimonrumble.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/zer8jfthndmxjbq/UP9000-SLUS01404_00-0000000000000001.pkg?dl=1'),
('51','Digimon World','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01032_00-0000000000000001','digimonworld.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/w0tgk3ff75baimi/UP9000-SLUS01032_00-0000000000000001.pkg?dl=1'),
('52','Digimon World 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01193_00-0000000000000001','digmonw2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/zinykh6ppj18go7/UP9000-SLUS01193_00-0000000000000001.pkg?dl=1'),
('53','Digimon World 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01436_00-0000000000000001','digmonw3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nub38r7r1ayj0j8/UP9000-SLUS01436_00-0000000000000001.pkg?dl=1'),
('54','Dino Crisis','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP0001-SLUS00922_00-0000111122223333','dinocrisis.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/rwkju9486s5e8iu/UP0001-SLUS00922_00-0000111122223333.pkg?dl=1'),
('55','Dino Crisis 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP0001-SLUS01279_00-0000111122223333','dinocrisis2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/hlmzy4ki889sed0/UP0001-SLUS01279_00-0000111122223333.pkg?dl=1'),
('56','Dino Crisis','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-NPUJ00922_00-0000000000000001','dinocrisis.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/s6jqlqac1assr3i/UP9000-NPUJ00922_00-0000000000000001.pkg?dl=1'),
('57','Dino Crisis FIX','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-NPUJ00922_00-FIX0000000000000','dinocrisis.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8mjfj32ab2e5n8m/UP9000-NPUJ00922_00-FIX0000000000000.pkg?dl=1'),
('58','Dracula CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES02762_00-0000000000000001','dracular.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/rcxlkmx7iwxv6f6/UP9000-SLES02762_00-0000000000000001.pkg?dl=1'),
('59','Dracula CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES12762_00-0000000000000001','dracular.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0xbmvf6fna6xvri/UP9000-SLES12762_00-0000000000000001.pkg?dl=1'),
('60','Dragon Ball GT FB','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00493_00-0000000000000001','dragonballfb.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/jo9n57s5g52nehi/UP9000-SLUS00493_00-0000000000000001.pkg?dl=1'),
('61','Driver','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES01816_00-0000000000000001','driver.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kwar04arm5vm3dn/UP9000-SLES01816_00-0000000000000001.pkg?dl=1'),
('62','Driver 2 CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01161_00-0000000000000001','driver2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/28cgepvy0txbg8s/UP9000-SLUS01161_00-0000000000000001.pkg?dl=1'),
('63','Driver 2 CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01161_00-0000000000000001','driver2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/hynaa8etjk5ml3b/UP9000-SLUS01161_00-0000000000000001.pkg?dl=1'),
('64','Echo Night','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00820_00-0000000000000001','echo.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/eho8z58g41xnhhq/UP9000-SLUS00820_00-0000000000000001.pkg?dl=1'),
('65','Ehrgeiz - God Bless the Ring','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00809_00-0000000000000001','ehrgeiz.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/zaprhjz53kc551b/UP9000-SLUS00809_00-0000000000000001.pkg?dl=1'),
('66','Gold and Glory The Road to El Dorado','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01312_00-0000000000000001','eldorado.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/osski1cq0goui28/UP9000-SLUS01312_00-0000000000000001.pkg?dl=1'),
('67','Final Fantasy 7 CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94163_00-0000000000000001','fantasy7.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8kaugdvjizu4qlb/UP9000-SCUS94163_00-0000000000000001.pkg?dl=1'),
('68','Final Fantasy 7 CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94163_00-0000000000000001','fantasy7.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/4i909lv9ucys5oh/UP9000-SCUS94163_00-0000000000000001.pkg?dl=1'),
('69','Final Fantasy 7 CD3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94163_00-0000000000000001','fantasy7.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/124yrmalmb9layq/UP9000-SCUS94163_00-0000000000000001.pkg?dl=1'),
('70','Final Fantasy 7 CD4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS94163_00-0000000000000001','fantasy7.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/2crn5pb6il3z5ew/UP9000-SLUS94163_00-0000000000000001.pkg?dl=1'),
('71','Final Fantasy 8 CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00892_00-0000000000000001','fantasy8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kii4cvsku6uiz6c/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1'),
('72','Final Fantasy 8 CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00892_00-0000000000000001','fantasy8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/4jo06pho0iuinln/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1'),
('73','Final Fantasy 8 CD3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00892_00-0000000000000001','fantasy8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/cm8qsox1g447fmd/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1'),
('74','Final Fantasy 8 CD4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00892_00-0000000000000001','fantasy8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/uqyxhke5u97rmts/UP9000-SLUS00892_00-0000000000000001.pkg?dl=1'),
('75','Final Fantasy 9 CD1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01251_00-0000000000000001','fantasy9.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/yo9x8rib578ngf4/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1'),
('76','Final Fantasy 9 CD2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01251_00-0000000000000001','fantasy9.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/lan14j67wwzt3b3/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1'),
('77','Final Fantasy 9 CD3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01251_00-0000000000000001','fantasy9.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/tqih2h18zuwbvw3/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1'),
('78','Final Fantasy 9 CD4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01251_00-0000000000000001','fantasy9.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/f06y83fgipzfw14/UP9000-SLUS01251_00-0000000000000001.pkg?dl=1'),
('79','Final Fantasy Chronicles','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01363_00-0000000000000001','ffchrono.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kw18ekl83zadehz/UP9000-SLUS01363_00-0000000000000001.pkg?dl=1'),
('80','Final Fantasy Tatics','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94221_00-0000000000000001','fftatics.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/z1k1fgpizve10rc/UP9000-SCUS94221_00-0000000000000001.pkg?dl=1'),
('81','Fishermans Bait Big Ol Bass 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01259_00-0000000000000001','fisherman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/26tuthcbqib2l9b/UP9000-SLUS01259_00-0000000000000001.pkg?dl=1'),
('82','Front Mission 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01011_00-0000000000000001','frontmission3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/9yzc0iyl9wt7nlg/UP9000-SLUS01011_00-0000000000000001.pkg?dl=1'),
('83','Grandia','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94457_00-0000000000000001','grandia1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/vwl4922ez4qfxgc/UP9000-SCUS94457_00-0000000000000001.pkg?dl=1'),
('84','Gran Turismo','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94194_00-0000000000000001','granturismo.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ss9cyvtmlb0caga/UP9000-SCUS94194_00-0000000000000001.pkg?dl=1'),
('85','Gran Turismo 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94488_00-0000000000000001','granturismo2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/o1jsfn17u6bcs0l/UP9000-SCUS94488_00-0000000000000001.pkg?dl=1'),
('86','GTA 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00106_00-0000000000000001','gta2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/mvp2ov6f5yj4sap/UP9000-SLUS00106_00-0000000000000001.pkg?dl=1'),
('87','Gunfighter The Legend of Jesse James','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03689_00-0000000000000001','gunfighter.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7q5nfztdjd9ge96/UP9000-SLES03689_00-0000000000000001.pkg?dl=1'),
('88','Harry Potter e a Câmara Secreta','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03973_00-0000000000000001','harrycs.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kf7dbfftqtxqo90/UP9000-SLES03973_00-0000000000000001.pkg?dl=1'),
('89','Harry Potter e a Pedra Filosofal','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03663_00-0000000000000001','harrypf.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fzadgwlm4exgj3f/UP9000-SLES03663_00-0000000000000001.pkg?dl=1'),
('90','Harvest Moon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01115_00-0000000000000001','harvestmoon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/h6u8j4yjcx0iwij/UP9000-SLUS01115_00-0000000000000001.pkg?dl=1'),
('91','Heart od Darkness','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00696_00-0000000000000001','heartofdarkness.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/zkb78whzoygf9ki/UP9000-SLUS00696_00-0000000000000001.pkg?dl=1'),
('92','Hoshigami Ruining Blue Earth','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01375_00-0000000000000001','blueearth.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/xu57q8k7sj1l7f2/UP9000-SLUS01375_00-0000000000000001.pkg?dl=1'),
('93','Hugo Quest for the Sunstones','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES02590_00-0000000000000001','hugo.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/gusgxjclku9f6k9/UP9000-SLES02590_00-0000000000000001.pkg?dl=1'),
('94','Inuyasha - A Feudal Fairy Tale','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01534_00-0000000000000001','inuyashafe.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bpdk2huzpb2a6a6/UP9000-SLUS01534_00-0000000000000001.pkg?dl=1'),
('95','Jackie Chan Stuntmaster','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00684_00-0000000000000001','jackchan.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0vo057fa8f85pjd/UP9000-SLUS00684_00-0000000000000001.pkg?dl=1'),
('96','Kagero Deception 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00677_00-0000000000000001','kagerod2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/v3s1f7wms1ojg32/UP9000-SLUS00677_00-0000000000000001.pkg?dl=1'),
('97','Klonoa - Door to Phantomile','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00585_00-0000000000000001','klonoa.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/50nf6i3uzhhqjaa/UP9000-SLUS00585_00-0000000000000001.pkg?dl=1'),
('98','Konami Arcade Classics','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00945_00-0000000000000001','konamiclassic.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/1gpiu54hu4utujb/UP9000-SLUS00945_00-0000000000000001.pkg?dl=1'),
('99','Legacy of Kain Soul Reaven','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00708_00-0000000000000001','legacyofkain1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bw133eiu6ril20u/UP9000-SLUS00708_00-0000000000000001.pkg?dl=1'),
('100','Legend of Legaia','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS94254_00-0000000000000001','legendoflegaia.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/rhukvrmke699fiv/UP9000-SLUS94254_00-0000000000000001.pkg?dl=1'),
('101','Legend of Mana','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01013_00-0000000000000001','legendofmana.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/e1lv1hu85x86h97/UP9000-SLUS01013_00-0000000000000001.pkg?dl=1'),
('102','Looney Tunes Racing','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01145_00-0000000000000001','looneytunesracing.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nwuaa04bbszhm3f/UP9000-SLUS01145_00-0000000000000001.pkg?dl=1'),
('103','Marvel x Capcom','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','FALTA CONTENT_ID','marvelvscapcom.jpg','2020-09-02 15:28:12','linkJogo'),
('104','MattHoffman BMX','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03973_00-0000000000000001','matthoffman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kf7dbfftqtxqo90/UP9000-SLES03973_00-0000000000000001.pkg?dl=1'),
('105','Medal of Honor','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01115_00-0000000000000001','medal.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/h6u8j4yjcx0iwij/UP9000-SLUS01115_00-0000000000000001.pkg?dl=1'),
('106','Medievil','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00696_00-0000000000000001','medievil.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/zkb78whzoygf9ki/UP9000-SLUS00696_00-0000000000000001.pkg?dl=1'),
('107','Medievil2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES02590_00-0000000000000001','medievil2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/gusgxjclku9f6k9/UP9000-SLES02590_00-0000000000000001.pkg?dl=1'),
('108','MegaMan8','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01534_00-0000000000000001','megaman8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bpdk2huzpb2a6a6/UP9000-SLUS01534_00-0000000000000001.pkg?dl=1'),
('109','MegaMan Legends','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00684_00-0000000000000001','megamanlegends.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0vo057fa8f85pjd/UP9000-SLUS00684_00-0000000000000001.pkg?dl=1'),
('110','MegaMan Legends2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00677_00-0000000000000001','megamanlegends2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/v3s1f7wms1ojg32/UP9000-SLUS00677_00-0000000000000001.pkg?dl=1'),
('111','MegaManX4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00585_00-0000000000000001','megamanx4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/50nf6i3uzhhqjaa/UP9000-SLUS00585_00-0000000000000001.pkg?dl=1'),
('112','MegaMan X5','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00945_00-0000000000000001','megamanx5.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/1gpiu54hu4utujb/UP9000-SLUS00945_00-0000000000000001.pkg?dl=1'),
('113','MegaMan X6','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00708_00-0000000000000001','megamanx6.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bw133eiu6ril20u/UP9000-SLUS00708_00-0000000000000001.pkg?dl=1'),
('114','Metal Gear','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS94254_00-0000000000000001','metalgear.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/rhukvrmke699fiv/UP9000-SLUS94254_00-0000000000000001.pkg?dl=1'),
('115','Metal SlugX','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01013_00-0000000000000001','metalslugx.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/e1lv1hu85x86h97/UP9000-SLUS01013_00-0000000000000001.pkg?dl=1'),
('116','Mortal Kombat4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01145_00-0000000000000001','mk4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nwuaa04bbszhm3f/UP9000-SLUS01145_00-0000000000000001.pkg?dl=1'),
('117','Mortal Kombat SF','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01059_00-0000000000000001','mksf.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/gn1tdpeqixlv0jd/UP9000-SLUS01059_00-0000000000000001.pkg?dl=1'),
('118','Mortal','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01113_00-0000000000000001','mortalkombatmsz.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/udz6s5h816nfywg/UP9000-SLUS01113_00-0000000000000001.pkg?dl=1'),
('119','Mortal Trilogy','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00974_00-0000000000000001','mortalkombattrilogy.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/y3tdqg5jm6h4iun/UP9000-SLUS00974_00-0000000000000001.pkg?dl=1'),
('120','Need for Speed','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94227_00-0000000000000001','nfs.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/9qoixwwg17zvkf1/UP9000-SCUS94227_00-0000000000000001.pkg?dl=1'),
('121','Need2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94564_00-0000000000000001','nfs2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kiz4d6r1luswfm1/UP9000-SCUS94564_00-0000000000000001.pkg?dl=1'),
('122','Need3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00453_00-0000000000000001','nfs3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bwwtvpuw3ofc2a7/UP9000-SLUS00453_00-0000000000000001.pkg?dl=1'),
('123','Need High Stakes','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00603_00-0000000000000001','nfshigh.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ml44v46qul0m008/UP9000-SLUS00603_00-0000000000000001.pkg?dl=1'),
('124','Need Porche','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01140_00-0000000000000001','nfsporche.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/78rqej7l4bpnh06/UP9000-SLUS01140_00-0000000000000001.pkg?dl=1'),
('125','Need Rally1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00561_00-0000000000000001','nfsrally.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/twkak4lcozbdzpi/UP9000-SLUS00561_00-0000000000000001.pkg?dl=1'),
('126','Need Rally2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01334_00-0000000000000001','nfsrally2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bwwhup5xvyq5mcb/UP9000-SLUS01334_00-0000000000000001.pkg?dl=1'),
('127','ParasiteEve','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01395_00-0000000000000001','parasite.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/es0vzk2v1v1l9ns/UP9000-SLUS01395_00-0000000000000001.pkg?dl=1'),
('128','ParasiteEve2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01156_00-0000000000000001','parasite2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/5ihtvcqg2xpg5yu/UP9000-SLUS01156_00-0000000000000001.pkg?dl=1'),
('129','Pinball3D','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01212_00-0000000000000001','pitfall3d.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/987l3fq8ctwuuck/UP9000-SLUS01212_00-0000000000000001.pkg?dl=1'),
('130','Resident Evil1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00605_00-0000000000000001','resident1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/57a8c0s1qrb0j3l/UP9000-SLUS00605_00-0000000000000001.pkg?dl=1'),
('131','Resident 2 Claire CD','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00824_00-0000000000000001','resident2claire.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/5a541iupspbnk72/UP9000-SLUS00824_00-0000000000000001.pkg?dl=1'),
('132','Resident 2 Leon CD','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','FALTA CONTENT_ID','resident2leon.jpg','2020-09-02 15:28:12','linkJogo'),
('133','Resident Evil3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00330_00-0000000000000001','resident3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/jw014t6bcy8ck15/UP9000-SLUS00330_00-0000000000000001.pkg?dl=1'),
('134','Road Rash','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00204_00-0000000000000001','roadrash.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nns2evyvd7scyh9/UP9000-SLUS00204_00-0000000000000001.pkg?dl=1'),
('135','Samurai Shodown','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00276_00-0000000000000001','samuraishodown.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/2aukbdamo9klfnk/UP9000-SLUS00276_00-0000000000000001.pkg?dl=1'),
('136','Silent Hill','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00620_00-0000000000000001','silenthill1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/jkdm3e5hgw5lqps/UP9000-SLUS00620_00-0000000000000001.pkg?dl=1'),
('137','Spiderman','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00826_00-0000000000000001','spiderman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/641wfu5p5lyzw2e/UP9000-SLUS00826_00-0000000000000001.pkg?dl=1'),
('138','spiderman2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01104_00-0000000000000001','spiderman2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/vgt4l3q84iq4zku/UP9000-SLUS01104_00-0000000000000001.pkg?dl=1'),
('139','Spyro','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00590_00-0000000000000001','spyrothedragon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/s87lojypef66d4l/UP9000-SLUS00590_00-0000000000000001.pkg?dl=1'),
('140','StreetEX Plus Alpha','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01003_00-0000000000000001','streetplusalfa.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6club3g2mujd0kq/UP9000-SLUS01003_00-0000000000000001.pkg?dl=1'),
('141','Sunikoden','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00662_00-0000000000000001','suikoden1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ezfemg52e1itgzc/UP9000-SLUS00662_00-0000000000000001.pkg?dl=1'),
('142','Super Shot Soccer','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01042_00-0000000000000001','superhot.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/tryo5b6fj9r46xg/UP9000-SLUS01042_00-0000000000000001.pkg?dl=1'),
('143','Syphon Filter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00254_00-0000000000000001','syphonfilter.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6cwfhpu7qxqjy4t/UP9000-SLUS00254_00-0000000000000001.pkg?dl=1'),
('144','Syphon Filter3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00170_00-0000000000000001','syphonphilter3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/h6xhsq547kip5y5/UP9000-SLUS00170_00-0000000000000001.pkg?dl=1'),
('145','Tenchu','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00756_00-0000000000000001','tenchu1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8w0zsdz9uq3ebpj/UP9000-SLUS00756_00-0000000000000001.pkg?dl=1'),
('146','Tenchu2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00748_00-0000000000000001','tenchu2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/1ihzxz4f4z9vhfb/UP9000-SLUS00748_00-0000000000000001.pkg?dl=1'),
('147','Tony Hawnk','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00923_00-0000000000000001','thawk.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/m9lq61m5oza75xt/UP9000-SLUS00923_00-0000000000000001.pkg?dl=1'),
('148','Tony Hawnk2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00035_00-0000000000000001','thawk2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qxypjrwqjiy9kng/UP9000-SLUS00035_00-0000000000000001.pkg?dl=1'),
('149','Tony Hawnk3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01039_00-0000000000000001','thawk3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/mftg3ndr2wofk4x/UP9000-SLUS01039_00-0000000000000001.pkg?dl=1'),
('150','Tony Hawnk4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00707_00-0000000000000001','thawk4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fzjnlgy27ilfhru/UP9000-SLUS00707_00-0000000000000001.pkg?dl=1'),
('151','The Legend of Dragon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00875_00-0000000000000001','thelegendofdragoon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fure26btiqk4tg1/UP9000-SLUS00875_00-0000000000000001.pkg?dl=1'),
('152','Tomba','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01378_00-0000000000000001','tomba.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/xdofdajt5sl361h/UP9000-SLUS01378_00-0000000000000001.pkg?dl=1'),
('153','Tomba','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94228_00-0000000000000001','tomba2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/spaufpcfy4qwi47/UP9000-SCUS94228_00-0000000000000001.pkg?dl=1'),
('154','Tomb Raider1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00548_00-0000000000000001','tombraider1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/et1p077hnf71j82/UP9000-SLUS00548_00-0000000000000001.pkg?dl=1'),
('155','Tomb Raider2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00292_00-0000000000000001','tombraider2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kqzyrisbqjs3n6d/UP9000-SLUS00292_00-0000000000000001.pkg?dl=1'),
('156','Tomb Raider3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01464_00-0000000000000001','tombraider3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/34ng9n7xnvtjf3q/UP9000-SLUS01464_00-0000000000000001.pkg?dl=1'),
('157','Tomb Chronicles','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94240_00-0000000000000001','tombraiderchronicles.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/y7ssxq6h6l5sla9/UP9000-SCUS94240_00-0000000000000001.pkg?dl=1'),
('158','Raider Last Revelation','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94640_00-0000000000000001','tombraiderlastrevelation.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/s9tiwjuja2d2zwo/UP9000-SCUS94640_00-0000000000000001.pkg?dl=1'),
('159','Twisted Metal','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00706_00-0000000000000001','twisted.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0r9bof6923a7vfa/UP9000-SLUS00706_00-0000000000000001.pkg?dl=1'),
('160','Twisted Metal3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00939_00-0000000000000001','twisted3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/987jzgbuel6sf7c/UP9000-SLUS00939_00-0000000000000001.pkg?dl=1'),
('161','Twisted Metal4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00860_00-0000000000000001','twisted4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8cfzvrfrt7obrkq/UP9000-SLUS00860_00-0000000000000001.pkg?dl=1'),
('162','Twisted Metal Brawl','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES02908_00-0000000000000001','twistedsb.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qp6gyltnsscsj1c/UP9000-SLES02908_00-0000000000000001.pkg?dl=1'),
('163','Vagrant','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03645_00-0000000000000001','vagrant.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qwbuqh50yyqik2g/UP9000-SLES03645_00-0000000000000001.pkg?dl=0'),
('164','Valkyrie','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01485_00-0000000000000001','valkyrie.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/3aaaz930n8ssy4l/UP9000-SLUS01485_00-0000000000000001.pkg?dl=1'),
('165','Vigilante8','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS94491_00-0000000000000001','vigilante8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/9nxoyv7bkk4ahxk/UP9000-SLUS94491_00-0000000000000001.pkg?dl=1'),
('166','Vigilante8 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94236_00-0000000000000001','vigilante82.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/knugy0ytyc3aaed/UP9000-SCUS94236_00-0000000000000001.pkg?dl=1'),
('167','Warcraft2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94454_00-0000000000000001','warcraft2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/41x4jo0b0rcymg3/UP9000-SCUS94454_00-0000000000000001.pkg?dl=1'),
('168','The Warriors','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00152_00-0000000000000001','warriors.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/62apz0yigw43z1s/UP9000-SLUS00152_00-0000000000000001.pkg?dl=1'),
('169','Wild Arms','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00437_00-0000000000000001','wildarms.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/wcrzdzj24oc9gf9/UP9000-SLUS00437_00-0000000000000001.pkg?dl=1'),
('170','Worlds Policies Chases','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00691_00-0000000000000001','wspolicechases.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/r090wfxpqtdmw2c/UP9000-SLUS00691_00-0000000000000001.pkg?dl=1'),
('171','Xenogears','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01311_00-0000000000000001','xenogears.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7wjggbn9dpknpxn/UP9000-SLUS01311_00-0000000000000001.pkg?dl=1'),
('172','Yu-Gi-Oh','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00885_00-0000000000000001','yugiohmemories.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7qg2ehq79fr6hj5/UP9000-SLUS00885_00-0000000000000001.pkg?dl=1'),
('173','Marvel x Capcom','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01059_00-0000000000000001','marvelvscapcom.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/gn1tdpeqixlv0jd/UP9000-SLUS01059_00-0000000000000001.pkg?dl=1'),
('174','Matt Hoffmans Pro BMX','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01113_00-0000000000000001','matthoffman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/udz6s5h816nfywg/UP9000-SLUS01113_00-0000000000000001.pkg?dl=1'),
('175','Medal of Honor','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00974_00-0000000000000001','medal.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/y3tdqg5jm6h4iun/UP9000-SLUS00974_00-0000000000000001.pkg?dl=1'),
('176','Medievil','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94227_00-0000000000000001','medievil.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/9qoixwwg17zvkf1/UP9000-SCUS94227_00-0000000000000001.pkg?dl=1'),
('177','Medievil 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94564_00-0000000000000001','medievil2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kiz4d6r1luswfm1/UP9000-SCUS94564_00-0000000000000001.pkg?dl=1'),
('178','MegaMan 8','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00453_00-0000000000000001','megaman8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bwwtvpuw3ofc2a7/UP9000-SLUS00453_00-0000000000000001.pkg?dl=1'),
('179','MegaMan Legends','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00603_00-0000000000000001','megamanlegends.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ml44v46qul0m008/UP9000-SLUS00603_00-0000000000000001.pkg?dl=1'),
('180','MegaMan Legends 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01140_00-0000000000000001','megamanlegends2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/78rqej7l4bpnh06/UP9000-SLUS01140_00-0000000000000001.pkg?dl=1'),
('181','MegaMan X3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00353_00-0000000000000001','megamanx3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ufkavndkvtefoje/UP9000-SLUS00353_00-0000000000000001.pkg?dl=1'),
('182','MegaMan X4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00561_00-0000000000000001','megamanx4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/25b836r80ko0u43/UP9000-SLUS00561_00-0000000000000001.pkg?dl=1'),
('183','MegaMan X5','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01334_00-0000000000000001','megamanx5.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/bwwhup5xvyq5mcb/UP9000-SLUS01334_00-0000000000000001.pkg?dl=1'),
('184','MegaMan X6','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01395_00-0000000000000001','megamanx6.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/es0vzk2v1v1l9ns/UP9000-SLUS01395_00-0000000000000001.pkg?dl=1'),
('185','Metal Gear Solid','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00594_00-0000000000000001','metalgear.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0oc9k6mjbthmo53/UP9000-SLUS00594_00-0000000000000001.pkg?dl=1'),
('186','Metal Gear Solid VR Missions (1999)','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00594_00-0000000000000001','metalgearvr.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/3sp8z76f6qi0usd/UP9000-SLUS00594_00-0000000000000001.pkg?dl=1'),
('187','Metal Slug X','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00957_00-0000000000000001','metalslugx.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/whdeifim4kb8unp/UP9000-SLUS00957_00-0000000000000001.pkg?dl=1'),
('188','Mickeys Wild Adventure (1996)','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01212_00-0000000000000001','mickey.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/987l3fq8ctwuuck/UP9000-SLUS01212_00-0000000000000001.pkg?dl=1'),
('189','Millennium Soldier  Expendable','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCES00163_00-0000000000000001','millennium.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/l27r6ck24xkumoz/UP9000-SCES00163_00-0000000000000001.pkg?dl=1'),
('190','Monster Racer','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES01716_00-0000000000000001','monsterracer.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/29ok4g88v8cd7nz/UP9000-SLES01716_00-0000000000000001.pkg?dl=1'),
('191','Monsters,Inc (2001)','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03246_00-0000000000000001','monsters.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kxbyez002fa3cjs/UP9000-SLES03246_00-0000000000000001.pkg?dl=1'),
('192','Mortal Kombat 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCES03769_00-0000000000000001','mk4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/uuzy54ja76ncdkg/UP9000-SCES03769_00-0000000000000001.pkg?dl=1'),
('193','Mortal Kombat Special Forces','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00605_00-0000000000000001','mksf.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0ztum7d1wq16w3a/UP9000-SLUS00605_00-0000000000000001.pkg?dl=1'),
('194','Mortal Kombat Mythologies Sub-Zero','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00824_00-0000000000000001','mortalkombatmsz.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/5a541iupspbnk72/UP9000-SLUS00824_00-0000000000000001.pkg?dl=1'),
('195','Mortal Kombat Trilogy','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','FALTA CONTENT_ID','mortalkombattrilogy.jpg','2020-09-02 15:28:12','linkJogo'),
('196','Necronomicon O Despertar das Trevas','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00330_00-0000000000000001','necronomicon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/jw014t6bcy8ck15/UP9000-SLUS00330_00-0000000000000001.pkg?dl=1'),
('197','Need for Speed The Road &amp; Track Presents','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03498_00-0000000000000001','nfs.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/h8jzrf1506x1wmy/UP9000-SLES03498_00-0000000000000001.pkg?dl=1'),
('198','Need for Speed 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES13498_00-0000000000000001','nfs2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/j45evvhj5h7zcjs/UP9000-SLES13498_00-0000000000000001.pkg?dl=1'),
('199','Need for Speed 3 - Hot Pursuit','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00204_00-0000000000000001','nfs3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nns2evyvd7scyh9/UP9000-SLUS00204_00-0000000000000001.pkg?dl=1'),
('200','Need for Speed - High Stakes','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00276_00-0000000000000001','nfshigh.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/2aukbdamo9klfnk/UP9000-SLUS00276_00-0000000000000001.pkg?dl=1'),
('201','Need for Speed - Porsche Unleashed','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00620_00-0000000000000001','nfsporche.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/jkdm3e5hgw5lqps/UP9000-SLUS00620_00-0000000000000001.pkg?dl=1'),
('202','Need for Speed - V-Rally','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00826_00-0000000000000001','nfsrally.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/641wfu5p5lyzw2e/UP9000-SLUS00826_00-0000000000000001.pkg?dl=1'),
('203','Need for Speed - V-Rally 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01104_00-0000000000000001','nfsrally2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/vgt4l3q84iq4zku/UP9000-SLUS01104_00-0000000000000001.pkg?dl=1'),
('204','Nicktoons Racing','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00590_00-0000000000000001','nicktoons.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/s87lojypef66d4l/UP9000-SLUS00590_00-0000000000000001.pkg?dl=1'),
('205','Nightmare Creatures 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01003_00-0000000000000001','nightmare2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6club3g2mujd0kq/UP9000-SLUS01003_00-0000000000000001.pkg?dl=1'),
('206','Parasite Eve','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03153_00-0000000000000001','parasite.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6yrbiaqgnh21jsh/UP9000-SLES03153_00-0000000000000001.pkg?dl=1'),
('207','Parasite Eve 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01112_00-0000000000000001','parasite2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/d2224xqcbu5uq1r/UP9000-SLUS01112_00-0000000000000001.pkg?dl=1'),
('208','Pitfall 3D - Beyond The Jungle','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00662_00-0000000000000001','pitfall3d.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ezfemg52e1itgzc/UP9000-SLUS00662_00-0000000000000001.pkg?dl=1'),
('209','Resident Evil','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01042_00-0000000000000001','resident1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/tryo5b6fj9r46xg/UP9000-SLUS01042_00-0000000000000001.pkg?dl=1'),
('210','Resident Evil 2 Clarie','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00254_00-0000000000000001','resident2claire.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6cwfhpu7qxqjy4t/UP9000-SLUS00254_00-0000000000000001.pkg?dl=1'),
('211','Resident Evil 2 Leon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00170_00-0000000000000001','resident2leon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/h6xhsq547kip5y5/UP9000-SLUS00170_00-0000000000000001.pkg?dl=1'),
('212','Resident Evil 3 Nemesis Ultimate Edition','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00756_00-0000000000000001','resident3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8w0zsdz9uq3ebpj/UP9000-SLUS00756_00-0000000000000001.pkg?dl=1'),
('213','Road Rash','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00748_00-0000000000000001','roadrash.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/1ihzxz4f4z9vhfb/UP9000-SLUS00748_00-0000000000000001.pkg?dl=1'),
('214','Samurai Showdown Warriors Rage','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00923_00-0000000000000001','samuraishodown.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/m9lq61m5oza75xt/UP9000-SLUS00923_00-0000000000000001.pkg?dl=1'),
('215','Silent Hill','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00035_00-0000000000000001','silenthill1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qxypjrwqjiy9kng/UP9000-SLUS00035_00-0000000000000001.pkg?dl=1'),
('216','Shadow Man','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01039_00-0000000000000001','shadowman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/mftg3ndr2wofk4x/UP9000-SLUS01039_00-0000000000000001.pkg?dl=1'),
('217','Sheep Raider  O Coiote','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00707_00-0000000000000001','sheepraider.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fzjnlgy27ilfhru/UP9000-SLUS00707_00-0000000000000001.pkg?dl=1'),
('218','Sol Divide','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00895_00-0000000000000001','soldivide.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/j7gmtof73ym38h7/UP9000-SLUS00895_00-0000000000000001.pkg?dl=1'),
('219','Spider Man','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01369_00-0000000000000001','spiderman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/1bodzcqr2nvndmf/UP9000-SLUS01369_00-0000000000000001.pkg?dl=1'),
('220','Spider-man 2 Enter Electro','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01519_00-0000000000000001','spiderman2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/mf7kqc3y5nhpte8/UP9000-SLUS01519_00-0000000000000001.pkg?dl=1'),
('221','Spyro the Dragon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00875_00-0000000000000001','spyrothedragon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fure26btiqk4tg1/UP9000-SLUS00875_00-0000000000000001.pkg?dl=1'),
('222','Street Fighter EX Plus Alpha','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01378_00-0000000000000001','streetplusalfa.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/xdofdajt5sl361h/UP9000-SLUS01378_00-0000000000000001.pkg?dl=1'),
('223','Street Fighter EX 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94228_00-0000000000000001','streetex2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/spaufpcfy4qwi47/UP9000-SCUS94228_00-0000000000000001.pkg?dl=1'),
('224','Stuart Little 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00548_00-0000000000000001','stuart2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/et1p077hnf71j82/UP9000-SLUS00548_00-0000000000000001.pkg?dl=1'),
('225','Sunikoden','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01105_00-0000000000000001','suikoden1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/upkodqvabk9sx60/UP9000-SLUS01105_00-0000000000000001.pkg?dl=1'),
('226','Super Shot Soccer','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94669_00-0000000000000001','superhot.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/vsrv1f3ikw1eg62/UP9000-SCUS94669_00-0000000000000001.pkg?dl=1'),
('227','Syphon Filter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00292_00-0000000000000001','syphonfilter.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/kqzyrisbqjs3n6d/UP9000-SLUS00292_00-0000000000000001.pkg?dl=1'),
('228','Syphon Filter 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01464_00-0000000000000001','syphonphilter3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/34ng9n7xnvtjf3q/UP9000-SLUS01464_00-0000000000000001.pkg?dl=1'),
('229','Tekken','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94240_00-0000000000000001','tekken.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/y7ssxq6h6l5sla9/UP9000-SCUS94240_00-0000000000000001.pkg?dl=1'),
('230','TEKKEN 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94640_00-0000000000000001','tekken2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/s9tiwjuja2d2zwo/UP9000-SCUS94640_00-0000000000000001.pkg?dl=1'),
('231','TEKKEN 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00006_00-0000000000000001','tekken3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/f8t2r3xovacvff3/UP9000-SLUS00006_00-0000000000000001.pkg?dl=1'),
('232','Tenchu Stealth Assassins','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLPS00300_00-0000000000000001','tenchu1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/6bbvpdra7nbsysa/UP9000-SLPS00300_00-0000000000000001.pkg?dl=1'),
('233','Tenchu 2 Birth of the Stealth Assassins','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLPS01300_00-0000000000000001','tenchu2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/075sjqgwur91zd6/UP9000-SLPS01300_00-0000000000000001.pkg?dl=1'),
('234','Tony Hawks Pro Skater','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00706_00-0000000000000001','thawk.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0r9bof6923a7vfa/UP9000-SLUS00706_00-0000000000000001.pkg?dl=1'),
('235','Tony Hawks Pro Skater 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00939_00-0000000000000001','thawk2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/987jzgbuel6sf7c/UP9000-SLUS00939_00-0000000000000001.pkg?dl=1'),
('236','Tony Hawks Pro Skater 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00860_00-0000000000000001','thawk3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8cfzvrfrt7obrkq/UP9000-SLUS00860_00-0000000000000001.pkg?dl=1'),
('237','Tony Hawks Pro Skater 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES02908_00-0000000000000001','thawk4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qp6gyltnsscsj1c/UP9000-SLES02908_00-0000000000000001.pkg?dl=1'),
('238','The Legend of Dragon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES03645_00-0000000000000001','thelegendofdragoon.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/qwbuqh50yyqik2g/UP9000-SLES03645_00-0000000000000001.pkg?dl=0'),
('239','Tomba','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01485_00-0000000000000001','tomba.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/3aaaz930n8ssy4l/UP9000-SLUS01485_00-0000000000000001.pkg?dl=1'),
('240','Tomba 2 The Evil Swine Returns','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS94491_00-0000000000000001','tomba2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/9nxoyv7bkk4ahxk/UP9000-SLUS94491_00-0000000000000001.pkg?dl=1'),
('241','Tomb Raider','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCES01331_00-0000000000000001','tombraider1.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/8ejj01c5epmzovi/UP9000-SCES01331_00-0000000000000001.pkg?dl=1'),
('242','Tomb Raider 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94454_00-0000000000000001','tombraider2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/cfc4cn7iygy649m/UP9000-SCUS94454_00-0000000000000001.pkg?dl=1'),
('243','Tomb Raider 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00152_00-0000000000000001','tombraider3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/62apz0yigw43z1s/UP9000-SLUS00152_00-0000000000000001.pkg?dl=1'),
('244','Tomb Raider Chronicles','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00437_00-0000000000000001','tombraiderchronicles.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/wcrzdzj24oc9gf9/UP9000-SLUS00437_00-0000000000000001.pkg?dl=1'),
('245','Tomb Raider - The Last Revelation Croft','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00691_00-0000000000000001','tombraiderlastrevelation.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/r090wfxpqtdmw2c/UP9000-SLUS00691_00-0000000000000001.pkg?dl=1'),
('246','Twisted Metal','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01311_00-0000000000000001','twisted.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7wjggbn9dpknpxn/UP9000-SLUS01311_00-0000000000000001.pkg?dl=1'),
('247','Twisted Metal 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00885_00-0000000000000001','twisted2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/7qg2ehq79fr6hj5/UP9000-SLUS00885_00-0000000000000001.pkg?dl=1'),
('248','Twisted Metal 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCES00061_00-0000000000000001','twisted3.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/g9of7bd1ghymb1g/UP9000-SCES00061_00-0000000000000001.pkg?dl=1'),
('249','Twisted Metal 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94306_00-0000000000000001','twisted4.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nmwc60qn0r53rsi/UP9000-SCUS94306_00-0000000000000001.pkg?dl=1'),
('250','Twisted Metal Small Brawl','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94249_00-0000000000000001','twistedsb.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/k9s2ryq114ziwo3/UP9000-SCUS94249_00-0000000000000001.pkg?dl=1'),
('251','Ultraman Fighting Evolution','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94560_00-0000000000000001','ultraman.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/uasxsicytetftg2/UP9000-SCUS94560_00-0000000000000001.pkg?dl=1'),
('252','Vagrant Story','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94642_00-0000000000000001','vagrant.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/k2pb3ozjk7uf4uv/UP9000-SCUS94642_00-0000000000000001.pkg?dl=1'),
('253','Valryrie Profile','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLPS01248_00-0000000000000001','valkyrie.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/j0xhzopqtzhoxdu/UP9000-SLPS01248_00-0000000000000001.pkg?dl=1'),
('254','Vigilante8','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01040_00-0000000000000001','vigilante8.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/abhfdjvhekqmpe9/UP9000-SLUS01040_00-0000000000000001.pkg?dl=1'),
('255','Vigilante8 2nd Offense','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01156_00-0000000000000001','vigilante82.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ep55bfr120vc1w7/UP9000-SLUS01156_00-0000000000000001.pkg?dl=1'),
('256','Warcraft 2 The Dark Saga','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00510_00-0000000000000001','warcraft2.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/ccmy5ux8r7jd5uu/UP9000-SLUS00510_00-0000000000000001.pkg?dl=1'),
('257','The Warriors','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00868_00-0000000000000001','warriors.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/nmv0vxxt10la7po/UP9000-SLUS00868_00-0000000000000001.pkg?dl=1'),
('258','Wild Arms','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00480_00-0000000000000001','wildarms.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/0e3i0z20a118cj3/UP9000-SLUS00480_00-0000000000000001.pkg?dl=1'),
('259','Worlds Policies Chases','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP0000-SLUS21215_00-PS2CLASSICS00000','wspolicechases.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/hflqpbzenu7tnsz/UP0000-SLUS21215_00-PS2CLASSICS00000.pkg?dl=1'),
('260','X-Com - Terror from the Deep','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SCUS94608_00-0000000000000001','xcom.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/fgksjycvy0oxkvs/UP9000-SCUS94608_00-0000000000000001.pkg?dl=1'),
('261','X-Com - UFO Defense','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS01165_00-0000000000000001','xufo.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/pra3moudr304gn5/UP9000-SLUS01165_00-0000000000000001.pkg?dl=1'),
('262','Xenogears','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLES00077_00-0000000000000001','xenogears.jpg','2020-09-02 15:28:12','https://www.dropbox.com/s/va2jmftbmk6r7p3/UP9000-SLES00077_00-0000000000000001.pkg?dl=1'),
('263','Yu-Gi-Oh! Forbidden MemoriesSSS','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS1','UP9000-SLUS00141_00-0000000000000001','yugiohmemories.jpg','2020-09-02 21:00:24','https://www.dropbox.com/s/vjkwleo963ml53q/UP9000-SLUS00141_00-0000000000000001.pkg?dl=1');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_ps2`
--

CREATE TABLE `playstation_ps2` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_ps2`
--

INSERT INTO `playstation_ps2` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES
('3','89 Arcade Classics','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20273_00-PS2CLASSICS00000','89arcade.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/49ywthrxj6ai630/UP0000-SLUS20273_00-PS2CLASSICS00000.pkg?dl=1'),
('4','Altered Beast','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES53024_00-PS2CLASSICS00000','alteredbeast.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/brdw15r2idzeqir/EP0000-SLES53024_00-PS2CLASSICS00000.pkg?dl=1'),
('5','Anime Fighters Vol. 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','JP0000-SLPS25675_00-PS2CLASSICS00000','animefighters.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/g56fxzz2ke4ativ/JP0000-SLPS25675_00-PS2CLASSICS00000.pkg?dl=1'),
('6','Anime Hero 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS77447_00-PS2CLASSICS00000','animehero1.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/7fo952mraaxt7m2/UP0000-SLUS77447_00-PS2CLASSICS00000.pkg?dl=1'),
('7','Arc the Lad Twilight of the Spirits','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SCUS97231_00-PS2CLASSICS00000','arcladt.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ad2cbum5y0r6dc4/UP0000-SCUS97231_00-PS2CLASSICS00000.pkg?dl=1'),
('8','Armored Core 2 Another Age','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20249_00-PS2CLASSICS00000','armoredcore2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/iaq1221pjk7gima/UP0000-SLUS20249_00-PS2CLASSICS00000.pkg_signed.pkg?dl=1'),
('9','BOMBA PATCH 2018 União','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','bombapatch2018.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('10','Bad Boys 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES51772_00-PS2CLASSICS00000','badboys2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/h35bfachvmfcnrs/EP0000-SLES51772_00-PS2CLASSICS00000.pkg?dl=1'),
('11','Biker Mice From Mars','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21578_00-PS2CLASSICS00000','bikermice.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/mug5qskr8ivypdn/UP0000-SLUS21578_00-PS2CLASSICS00000.pkg?dl=1'),
('12','Black','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','black.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('13','Bleach Erabareshi Tamashi','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','JP0000-SCPS15087_00-PS2CLASSICS00000','bleachtamashi.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/utj6heq2whpwax8/JP0000-SCPS15087_00-PS2CLASSICS00000.pkg?dl=1'),
('14','Bloodyrayne 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20461_00-PS2CLASSICS00000','bloodyrayne1.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/qrr5o3m05vvgftm/UP0000-SLUS20461_00-PS2CLASSICS00000.pkg?dl=1'),
('15','Bully','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21269_00-PS2CLASSICS00000','bully.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/s5hxh41f24saesk/UP0000-SLUS21269_00-PS2CLASSICS00000.pkg?dl=1'),
('16','Burnout 3Takedown','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21050_00-PS2CLASSICS00000','burnout3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/izj5t5vqfgxjofk/UP0000-SLUS21050_00-PS2CLASSICS00000.pkg?dl=1'),
('17','Capcom Vs. SNK 2 Mark of the Millennium','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20246_00-PS2CLASSICS00000','cvss2jpg.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/zmn3seruso6q4vi/UP0000-SLUS20246_00-PS2CLASSICS00000.pkg?dl=1'),
('18','Castlevania Curse of Darkness','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES53755_00-PS2CLASSICS00000','castlevaniacurse.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/kqf7c04yy0d70sg/EP0000-SLES53755_00-PS2CLASSICS00000.pkg?dl=1'),
('19','Clock Tower 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20633_00-PS2CLASSICS00000','clocktower3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/v0o01w5np6nhl5a/UP0000-SLUS20633_00-PS2CLASSICS00000.pkg?dl=1'),
('20','Coldwinter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20845_00-PS2CLASSICS00000','coldwinter.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/gqxg9a1atwgad0v/UP0000-SLUS20845_00-PS2CLASSICS00000.pkg?dl=1'),
('21','Crash Bandicoot The wrath of Cortex','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20238_00-PS2CLASSICS00000','crashwhathofcortex.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/oplfpqhhxrkhadg/UP0000-SLUS20238_00-PS2CLASSICS00000.pkg?dl=1'),
('22','Crash Tag Team Racing','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21191_00-PS2CLASSICS00000','crashracing.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/jzxlncromba1q9a/UP0000-SLUS21191_00-PS2CLASSICS00000.pkg?dl=1'),
('23','Dark Watch','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES53564_00-PS2CLASSICS00000','darkwatch.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/1zz8ue8hsp4n58h/EP0000-SLES53564_00-PS2CLASSICS00000.pkg?dl=1'),
('24','Def Jam Fight for NY','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21004_00-PS2CLASSICS00000','defjamny.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/nit6gc81kzjqanj/UP0000-SLUS21004_00-PS2CLASSICS00000.pkg?dl=1'),
('25','Devil Kings','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES53870_00-PS2CLASSICS00000','devilkings.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/xuq6jwvlud5dsg2/EP0000-SLES53870_00-PS2CLASSICS00000.pkg?dl=1'),
('26','Devil May Cry 3 Special Edition','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES54186_00-PS2CLASSICS00000','dmc3se.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ne8qeiximl5pi6e/EP0000-SLES54186_00-PS2CLASSICS00000.pkg?dl=1'),
('27','Digimon World','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21598_00-PS2CLASSICS00000','digimonworld.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/28kh8qduyr9si2p/UP0000-SLUS21598_00-PS2CLASSICS00000.pkg?dl=1'),
('28','Dowhill Domination','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES52202_00-PS2CLASSICS00000','dowhilldm.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/v7jvkd0tgwa43d8/EP0000-SLES52202_00-PS2CLASSICS00000.pkg?dl=1'),
('29','Dragon Ball Z Budokai Tenkaichi 3 [PT','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21678_00-PS2CLASSICS00000','dbzbt4.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/kfv5z2sct9zw654/UP0000-SLUS21678_00-PS2CLASSICS00000.pkg?dl=1'),
('30','Dragon Ball Z Budokai Tenkaichi 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21678_00-PS2CLASSICS00000','dbzbt3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/mx9u94j1gyep7m1/UP0000-SLUS21678_00-PS2CLASSICS00000.pkg?dl=1'),
('31','Dragon BallZ Budokai Af','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20998_00-PS2CLASSICS00000','dbzbudokaiaf.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/csc1lcq8yoytrtp/UP0000-SLUS20998_00-PS2CLASSICS00000.pkg?dl=1'),
('32','Dragon BallZ Tenkaichi 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21441_00-PS2CLASSICS00000','dbztenkaichi2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/nufdt5h6q3p9f5g/UP0000-SLUS21441_00-PS2CLASSICS00000.pkg?dl=1'),
('33','Driver Parallel Lines','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21271_00-PS2CLASSICS00000','driverpl.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/bf2bmu62jev7ynt/UP0000-SLUS21271_00-PS2CLASSICS00000.pkg?dl=1'),
('34','Evil Dead Regeneration','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21048_00-PS2CLASSICS00000','evildeadreg.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/pcikm1th1dptkjv/UP0000-SLUS21048_00-PS2CLASSICS00000.pkg?dl=1'),
('35','Fatal Frame 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','fatalframe1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('36','Fatal Frame 2 Crimson Butterfly','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','fatalframe2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('37','Fatal Fury Battle Archives','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','fatalfurybattle.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('38','Fifa Street 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES53797_00-PS2CLASSICS00000','fifastreet2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/p8s6vtjjh0wpsq8/EP0000-SLES53797_00-PS2CLASSICS00000.pkg?dl=1'),
('39','Final Fantasy VII Dirge of Cerberus','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21419_00-PS2CLASSICS00000','ffviidirge.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/r8kqh2tbmb29sgx/UP0000-SLUS21419_00-PS2CLASSICS00000.pkg?dl=1'),
('40','Final Fantasy XII','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','ffxii.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('41','FlatOut 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','flatout2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('42','Futurama The Game','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','futurama.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('43','Genji','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Genji%20%5BPS2%20Classics%5D%20%5BSCES53328%5D','genji.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/dtfc7k7agplkh9t/Genji%20%5BPS2%20Classics%5D%20%5BSCES53328%5D.pkg_signed.pkg?dl=1'),
('44','God Hand','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','godhand.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('45','God of War','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SCUS97399_00-PS2CLASSICS00000','gow1.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/nnwxeh7ulzpuq76/UP0000-SCUS97399_00-PS2CLASSICS00000.pkg?dl=1'),
('46','Grand Theft Auto 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','gta3.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('47','Grand Theft Auto MOD Sonic Rings','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','gtasonic.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('48','Grand Theft Auto Liberty City Stories','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','gtalibertycitystories.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('49','Grand Theft Auto Vice City','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','gtavicecity2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('50','Grand Theft Auto Vice City Stories','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','gtavicecitystories.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('51','Guitar God 2.0','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21447_00-PS2CLASSICS00000','guitargod2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/au9wt3ahr6l6utw/UP0000-SLUS21447_00-PS2CLASSICS00000.pkg?dl=1'),
('52','Guitar God 3.0','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS35547_00-PS2CLASSICS00000','guitargod3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/7devussebfto7c2/UP0000-SLUS35547_00-PS2CLASSICS00000.pkg?dl=1'),
('53','Guitar Hero GOD 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21447_00-PS2CLASSICS00000','guitargod1.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/nejby445j0ydfbg/UP0000-SLUS21447_00-PS2CLASSICS00000.pkg?dl=1'),
('54','Harry Potter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20826_00-PS2CLASSICS00000','harrypss.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/q0kxtsx8212l8sq/UP0000-SLUS20826_00-PS2CLASSICS00000.pkg?dl=1'),
('55','Harry Potter Copa Mundial de Quadribol ','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20769_00-PS2CLASSICS00000','harryquadribol.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/8kixr5p46zt6zf6/UP0000-SLUS20769_00-PS2CLASSICS00000.pkg?dl=1'),
('56','Harry Potter and The Half Prince Blood','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21808_00-PS2CLASSICS00000','harryhpb.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/a6cqw1sa5bxcw47/UP0000-SLUS21808_00-PS2CLASSICS00000.pkg?dl=1'),
('57','Harry Potter e a Pedra Filosofal','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES52055_00-PS2CLASSICS00000','harryfilosofal.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/eesti7fezk7utje/EP0000-SLES52055_00-PS2CLASSICS00000.pkg?dl=1'),
('58','Haunting Ground','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21075_00-PS2CLASSICS00000','hauntingground.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/s8e3o456fj5zcl8/UP0000-SLUS21075_00-PS2CLASSICS00000.pkg?dl=1'),
('59','Herdy Gerdy','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES50751_00-PS2CLASSICS00000','herdygerdy.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/r2ishqe0n71u1gt/EP0000-SLES50751_00-PS2CLASSICS00000.pkg?dl=1'),
('60','Iron Man','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Iron%20Man%20%5BPS2%20Classics%5D%20%5BSLUS21739%5D','ironman.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/t8p58p17m53ruum/Iron%20Man%20%5BPS2%20Classics%5D%20%5BSLUS21739%5D.pkg_signed.pkg?dl=1'),
('61','Jackie Chan Adventure','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SCES52412_00-PS2CLASSICS00000','jackiechanadv.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ohlyuwazcj7fvlj/EP0000-SCES52412_00-PS2CLASSICS00000.pkg?dl=1'),
('62','Jak 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Jak%20II%20%5BPS2%20Classics%5D%20%5BSCUS97265%5D','jak2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/pywghb6zudnpp06/Jak%20II%20%5BPS2%20Classics%5D%20%5BSCUS97265%5D.pkg_signed.pkg?dl=1'),
('63','Jak X','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Jak%203%20%5BPS2%20Classics%5D%20%5BSCUS97330%5D','jakxcbracing.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/35hag2e437k3559/Jak%203%20%5BPS2%20Classics%5D%20%5BSCUS97330%5D.pkg_signed.pkg?dl=1'),
('64','Jak and Daxter The Lost Frontier','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Jak%20and%20Daxter%20-%20The%20Precursor%20Legacy%20%5BPS2%20Classics%5D%20%5BSCUS97124%5D','jakanddaxter.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/d97jdtqlmf3yvcb/Jak%20and%20Daxter%20-%20The%20Precursor%20Legacy%20%5BPS2%20Classics%5D%20%5BSCUS97124%5D.pkg_signed.pkg?dl=1'),
('65','Justice League','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Justice%20League%20Heroes%20%5BPS2%20Classics%5D%20%5BSLUS21304%5D','justiceleague.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ynun53m9josr8m0/Justice%20League%20Heroes%20%5BPS2%20Classics%5D%20%5BSLUS21304%5D.pkg_signed.pkg?dl=1'),
('66','Kingdom Hearts','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20370_00-PS2CLASSICS00000','kinghearts.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/4f9ifwlnjpnhtx3/UP0000-SLUS20370_00-PS2CLASSICS00000.pkg?dl=0'),
('67','Kingdom Hearts 1 Final Mix','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','JP0000-SLPS25198_00-PS2CLASSICS00000','kingdown.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ymgg3sig4d9gc6q/JP0000-SLPS25198_00-PS2CLASSICS00000.pkg?dl=1'),
('68','Kingdom Hearts 2 Final Mix','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','JP0000-SLPM66675_00-PS2CLASSICS00000','kingdomhearts1.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/sfj7nmwf306z8ex/JP0000-SLPM66675_00-PS2CLASSICS00000.pkg?dl=1'),
('69','Knight Rider','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES51011_00-PS2CLASSICS00000','knightrider.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/gq29023p5mozg3s/EP0000-SLES51011_00-PS2CLASSICS00000.pkg?dl=1'),
('70','Knight Rider 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES52836_00-PS2CLASSICS00000','knightrider2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/liy8n8zgdlj7uw1/EP0000-SLES52836_00-PS2CLASSICS00000.pkg?dl=1'),
('71','La Puccelle Tatics','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','lapucelletactics.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('72','Legaia 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','legaia2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('73','Looney Tunes Space Race','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','looneytunesspacerace.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('74','Lord Of The Ring The Fellowship Of The Ring','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20520_00-PS2CLASSICS00000','lordofring.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/bbj8htbf02w4o0y/UP0000-SLUS20520_00-PS2CLASSICS00000.pkg?dl=1'),
('75','Mafia 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','mafia1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('76','Magna Carta','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21221_00-PS2CLASSICS00000','magnacarta.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/93w3ijg0l5mq0r2/UP0000-SLUS21221_00-PS2CLASSICS00000.pkg?dl=1'),
('77','Manhunt 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','manhunt2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('78','Marvel Nemesis Rise Of The Imperfects','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21281_00-PS2CLASSICS00000','marvelnemesis.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/kdy1xapryl3qeen/UP0000-SLUS21281_00-PS2CLASSICS00000.pkg?dl=1'),
('79','Max Payne 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','maxpayne1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('80','Max Payne 2 Fall of Max Payne','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','maxpayne2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('81','Maximo 1 Ghosts to Glory','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','maximo1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('82','Maximo 2 Army of Zin','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','maximo2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('83','Medal of Honor','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21199_00-PS2CLASSICS00000','medalhonorassault.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/5qm7ajq0naaougf/UP0000-SLUS21199_00-PS2CLASSICS00000.pkg?dl=1'),
('84','Mega Man X8','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20960_00-PS2CLASSICS00000','megamanx8.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/uchy1o6u525wh5e/UP0000-SLUS20960_00-PS2CLASSICS00000.pkg?dl=1'),
('85','Metal Slug Complete','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','JP0000-SLPS25762_00-PS2CLASSICS00000','metalslugcomplete.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/pkdd5wdmy1umd8e/JP0000-SLPS25762_00-PS2CLASSICS00000.pkg?dl=1'),
('86','Midnight Club 3 DUB Edition Remix','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21355_00-PS2CLASSICS00000','midnight3dr.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/fwphssqolpa74w9/UP0000-SLUS21355_00-PS2CLASSICS00000.pkg?dl=1'),
('87','Mortal Kombat Armageddon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','mortakombatarmageddon.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('88','Mortal Kombat Deadly Alliance','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES50717_00-PS2CLASSICS00000','mkdeadly.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/eck0jjtb08h6k77/EP0000-SLES50717_00-PS2CLASSICS00000.pkg?dl=1'),
('89','Mortal Kombat Deception','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20881_00-PS2CLASSICS00000','mkdeception.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/1exyvnh1hga7das/UP0000-SLUS20881_00-PS2CLASSICS00000.pkg?dl=1'),
('90','Mortal Kombat Shaolin Monks','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21087_00-PS2CLASSICS00000','mkshaolin.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/zrqk4h0fwwhhcp6/UP0000-SLUS21087_00-PS2CLASSICS00000.pkg?dl=1'),
('91','Namco Vs. Capcom','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','namcoxcapcom.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('92','Narc','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20730_00-PS2CLASSICS00000','narc.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/l3134ad8c5bdu2a/UP0000-SLUS20730_00-PS2CLASSICS00000.pkg?dl=1'),
('93','Naruto Shippuden Ultimate Ninja 5','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES55605_00-PS2CLASSICS00000','naturoun5.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/nip0zk4burtw0js/EP0000-SLES55605_00-PS2CLASSICS00000.pkg_signed.pkg?dl=1'),
('94','Naruto ultimate Ninja 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21575_00-PS2CLASSICS00000','narultninja2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/wndipjo3kfhl2td/UP0000-SLUS21575_00-PS2CLASSICS00000.pkg?dl=1'),
('95','Naruto ultimate Ninja 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES55237_00-PS2CLASSICS00000','narultninja2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/leuy1e4js0frlzh/EP0000-SLES55237_00-PS2CLASSICS00000.pkg?dl=1'),
('96','Need for Speed Carbon','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21493_00-PS2CLASSICS00000','nfscarbon.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/dacf4o42x16cecg/UP0000-SLUS21493_00-PS2CLASSICS00000.pkg?dl=1'),
('97','Need for Speed Mostwanted Black Edition','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21351_00-PS2CLASSICS00000','nfsmostwanted.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/yufd7cgtkm0gklu/UP0000-SLUS21351_00-PS2CLASSICS00000.pkg?dl=1'),
('98','Need for Speed Underground','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21065_00-PS2CLASSICS00000','nfsunderground.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/2vvzco9sqaq0gfl/UP0000-SLUS21065_00-PS2CLASSICS00000.pkg?dl=1'),
('99','Neo Contra','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20961_00-PS2CLASSICS00000','neocontra.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/euiol1y89sardxe/UP0000-SLUS20961_00-PS2CLASSICS00000.pkg?dl=1'),
('100','Obscure 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','obscure1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('101','Obscure 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','obscure2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('102','Okami','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21115_00-PS2CLASSICS00000','okamips2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/pa4qa1k068jmyco/UP0000-SLUS21115_00-PS2CLASSICS00000.pkg?dl=1'),
('103','Onimusha 1 Warlords','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','onimusha1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('104','Onimusha 2 Samurais Destiny','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Onimusha%202%20-%20Samurai%27s%20Destiny%20%5BPS2%20Classics%5D%20%5BSLUS20393%5D','onimusha2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/rpyfcr99y66vtkp/Onimusha%202%20-%20Samurai%27s%20Destiny%20%5BPS2%20Classics%5D%20%5BSLUS20393%5D.pkg_signed.pkg?dl=1'),
('105','Onimusha 3 Demon Siege','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Onimusha%203%20-%20Demon%20Siege%20%5BPS2%20Classics%5D%20%5BSLUS20694%5D','onimusha3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/9054nae3syw5o1n/Onimusha%203%20-%20Demon%20Siege%20%5BPS2%20Classics%5D%20%5BSLUS20694%5D.pkg_signed.pkg?dl=1'),
('106','OutRun Coast 2 Coast','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21274_00-PS2CLASSICS00000','outrun.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/pl6bgwdyoc8z1mr/UP0000-SLUS21274_00-PS2CLASSICS00000.pkg?dl=1'),
('107','Persona 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21569_00-PS2CLASSICS00000','persona3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/gqr2ujgq3ibo0ks/UP0000-SLUS21569_00-PS2CLASSICS00000.pkg?dl=1'),
('108','Phantom Brave','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Phantom%20Brave%20%5BPS2%20Classics%5D%20%5BSLUS20955%5D','phantombrave.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/1iymhxso3at4vir/Phantom%20Brave%20%5BPS2%20Classics%5D%20%5BSLUS20955%5D.pkg?dl=1'),
('109','PitFall','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20408_00-PS2CLASSICS00000','pitfall.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/hlc5w6xlu60n07w/UP0000-SLUS20408_00-PS2CLASSICS00000.pkg?dl=1'),
('110','Prince of Persia Sands of Time','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20743_00-PS2CLASSICS00000','ppersiasot.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/khcb2dnx2migxk6/UP0000-SLUS20743_00-PS2CLASSICS00000.pkg?dl=1'),
('111','Resident Evil 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21134_00-PS2CLASSICS00000','resevil4.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/smljem2dzydpna3/UP0000-SLUS21134_00-PS2CLASSICS00000.pkg_signed.pkg?dl=1'),
('112','Resident Evil Outbreak','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES51589_00-PS2CLASSICS00000','residentoutbreak.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/bl5a2iwbkuogm07/EP0000-SLES51589_00-PS2CLASSICS00000.pkg?dl=1'),
('113','Resident Evil Code Veronica X','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','residentcodeveronica.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('114','Resident Evil Dead Aim','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES51448_00-PS2CLASSICS00000','residentdeadaim.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/cnbh0n2eafp1c9v/EP0000-SLES51448_00-PS2CLASSICS00000.pkg?dl=1'),
('115','Rogue Galaxy','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','roguegalaxy.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('116','Rule of Rose','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21448_00-PS2CLASSICS00000','ruleofrose.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ost7akb5xm7ndk7/UP0000-SLUS21448_00-PS2CLASSICS00000.pkg?dl=1'),
('117','Saint Seiya','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES54162_00-PS2CLASSICS00000','seiyasanctuary.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/bsip5lgmb0qde04/EP0000-SLES54162_00-PS2CLASSICS00000.pkg?dl=1'),
('118','Samurai Showdown Anthology','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21629_00-PS2CLASSICS00000','samuraishowdown.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/wx4ngoapjl2omst/UP0000-SLUS21629_00-PS2CLASSICS00000.pkg?dl=1'),
('119','Scarface The World is Yours','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Scarface%20-%20The%20World%20is%20Yours%20%5BPS2%20Classics%5D%20%5BSLUS21111%5D','scarface.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/ql9lutg82bnqkds/Scarface%20-%20The%20World%20is%20Yours%20%5BPS2%20Classics%5D%20%5BSLUS21111%5D.pkg_signed.pkg?dl=1'),
('120','Shadow of the Colossus','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','sotc.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('121','Shrek 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20745_00-PS2CLASSICS00000','shrek2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/z89wg16tyo61g65/UP0000-SLUS20745_00-PS2CLASSICS00000.pkg?dl=1'),
('122','Shrek Super Slam','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','EP0000-SLES53657_00-PS2CLASSICS00000','shreksuper.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/8m7jh0k68zcxj1x/EP0000-SLES53657_00-PS2CLASSICS00000.pkg?dl=1'),
('123','Shrek The Third','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21454_00-PS2CLASSICS00000','shrek3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/xcld4ywzqbzg2k4/UP0000-SLUS21454_00-PS2CLASSICS00000.pkg?dl=1'),
('124','Silent Hill 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20228_00-PS2CLASSICS00000','silenthill2.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/iaik48wjjrqh5x6/UP0000-SLUS20228_00-PS2CLASSICS00000.pkg?dl=1'),
('125','Silent Hill 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20622_00-PS2CLASSICS00000','silenthill3.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/fvwdwep4ggak5bw/UP0000-SLUS20622_00-PS2CLASSICS00000.pkg?dl=1'),
('126','Silent Hill 4 The Room','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20515_00-PS2CLASSICS00000','silenthill4.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/mqt6b0qx75jlko3/UP0000-SLUS20515_00-PS2CLASSICS00000.pkg?dl=1'),
('127','Silent Hill Shattered Memories','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21899_00-PS2CLASSICS00000','silenthillsm.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/dv8g8zy209nd63g/UP0000-SLUS21899_00-PS2CLASSICS00000.pkg?dl=1'),
('128','Siren','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SCUS97355_00-PS2CLASSICS00000','siren.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/yzju0hp3ezwkm8c/UP0000-SCUS97355_00-PS2CLASSICS00000.pkg?dl=1'),
('129','Spider Man 2','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','spiderman2.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('130','Splinter Cell 1','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','splintercell1.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('131','Splinter Cell 2 Pandora Tomorrow','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','splintercellpandoratomorrow.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('132','Splinter Cell Double Agent','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','splintercelldoubleagent.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('133','Star Wars StarFighter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','starwarsstarfighter.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('134','Syphon Filter The Omega Strain','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Syphon%20Filter%20-%20The%20Omega%20Strain%20%5BPS2%20Classics%5D%20%5BSCUS97264%5D','syphonomega.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/f3nmhxxhtrnuo6x/Syphon%20Filter%20-%20The%20Omega%20Strain%20%5BPS2%20Classics%5D%20%5BSCUS97264%5D.pkg_signed.pkg?dl=1'),
('135','The King Of Fighters The Orochi Saga','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21554_00-PS2CLASSICS00000','koforochi.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/oaiumcvgjlu2aoa/UP0000-SLUS21554_00-PS2CLASSICS00000.pkg?dl=1'),
('136','The King of Fighters 94 Re','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','tkof94.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('137','The King of Figthers 2002 Unlimited Match','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','tkof2002.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('138','The King of Figthers 98 Ultimate Match','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','tkof98.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('139','The King of Figthers NESTS','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','JP0000-SLPS25661_00-PS2CLASSICS00000','tkofnests.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/f02nnmbutq44ond/JP0000-SLPS25661_00-PS2CLASSICS00000.pkg?dl=1'),
('140','Time Spliter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20090_00-PS2CLASSICS00000','timespliter.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/66iqt3ciy5hapv8/UP0000-SLUS20090_00-PS2CLASSICS00000.pkg?dl=1'),
('141','Tony Hawks Pro Skater 4','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20504_00-PS2CLASSICS00000','tonyskater4.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/qb6sk9xmyp5f15k/UP0000-SLUS20504_00-PS2CLASSICS00000.pkg?dl=1'),
('142','Urban Reigh','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21209_00-PS2CLASSICS00000','urbanreigh.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/vrt6huqeoiz7vwt/UP0000-SLUS21209_00-PS2CLASSICS00000.pkg?dl=1'),
('143','Van Helsing','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20738_00-PS2CLASSICS00000','vanhelsing.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/lr86uvgr4z4azaw/UP0000-SLUS20738_00-PS2CLASSICS00000.pkg?dl=1'),
('144','Virtual Fighter 4 Evolution','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','vf4evo.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('145','Winning Eleven 10','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS20616_00-PS2CLASSICS00000','winning10.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/gc4x7hqff6ciftp/UP0000-SLUS20616_00-PS2CLASSICS00000.pkg?dl=1'),
('146','World Heroes Anthology','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','UP0000-SLUS21725_00-PS2CLASSICS00000','wha.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/xsb91cw7ii5bnq9/UP0000-SLUS21725_00-PS2CLASSICS00000.pkg?dl=1'),
('147','Yu','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','Yu-Gi-Oh%21%20The%20Duelists%20of%20the%20Roses%20%5BPS2%20Classics%5D%20%5BSLUS20515%5D','yugiohroses.jpg','2020-09-02 15:28:46','https://www.dropbox.com/s/u2vjskwmj11fjch/Yu-Gi-Oh%21%20The%20Duelists%20of%20the%20Roses%20%5BPS2%20Classics%5D%20%5BSLUS20515%5D.pkg?dl=1'),
('148','jak 3','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','jak3.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404'),
('149','jak and Daxter','Idioma: Ingles<br/> Legenda: PT-BR<br/> Plataforma: PS2','FALTA CONTENT_ID','jakdaxter.jpg','2020-09-02 15:28:46','http://tcxsproject.com.br/404');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_ps3`
--

CREATE TABLE `playstation_ps3` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link1` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link2` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link3` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link4` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link5` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link6` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link7` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link8` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link9` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link10` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link11` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link12` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link13` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link14` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link15` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link16` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link17` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link18` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link19` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link20` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link21` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link22` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link23` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link24` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link25` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link26` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link27` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link28` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link29` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `link30` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_ps3`
--

INSERT INTO `playstation_ps3` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link1`, `link2`, `link3`, `link4`, `link5`, `link6`, `link7`, `link8`, `link9`, `link10`, `link11`, `link12`, `link13`, `link14`, `link15`, `link16`, `link17`, `link18`, `link19`, `link20`, `link21`, `link22`, `link23`, `link24`, `link25`, `link26`, `link27`, `link28`, `link29`, `link30`) VALUES
('3','007 Goldeneye Reloaded','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPEB01292_00-NPEB012920000000','007gold.jpg','2020-09-02 15:51:36',
    'https://www.dropbox.com/s/w8ggtv07t34gwqw/1DGAME-NPEB01292_00-NPEB012920000000.pkg?dl=1','https://www.dropbox.com/s/w6sr8622ptkv44y/2DGAME-NPEB01292_00-NPEB012920000000.pkg?dl=1','https://www.dropbox.com/s/680g29hcergfby1/3DGAME-NPEB01292_00-NPEB012920000000.pkg?dl=1','https://www.dropbox.com/s/biy7t8hck5oe9er/2PATCH-BLES01292_00-BLES012920000000.pkg?dl=1','---','---','---','---','---','---','---','---','---',
    '---','---','','','','','','','','','','',
    '','','','',''),
('4','007 LEGENDS','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB30983_00-NPUB309830000000','007legend.jpg','2020-09-02 16:27:31',
    'https://www.dropbox.com/s/gin5qsgurzi7wcb/1DGAME-NPUB30983_00-NPUB309830000000.pkg?dl=1','https://www.dropbox.com/s/vdg38w9ag7r9dzy/2DGAME-NPUB30983_00-NPUB309830000000.pkg?dl=1','https://www.dropbox.com/s/yd41r66d66qeu0p/3DGAME-NPUB30983_00-NPUB309830000000.pkg?dl=1','https://www.dropbox.com/s/y0recn2t70w3tnt/2PATCH-BLUS30983_00-BLUS309830000000.pkg?dl=1','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('5','Assassin Creed 2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1HGAME-NPUB30423_00-NPUB304230000000','assassins2.jpg','2020-09-02 16:28:06',
    'https://www.dropbox.com/s/uek25rzfzyyotlv/1HGAME-NPUB30423_00-NPUB304230000000.pkg?dl=1','https://www.dropbox.com/s/asmejqitsljkzqi/2HGAME-NPUB30423_00-NPUB304230000000.pkg?dl=1','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('6','Assassin Creed 3','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB30991_00-NPUB309910000000','assassins3.jpg','2020-09-02 16:28:11',
    'https://www.dropbox.com/s/xjcut61k02x5osg/1DGAME-NPUB30991_00-NPUB309910000000.pkg?dl=1','https://www.dropbox.com/s/b9dlkrwoq89zemy/2DGAME-NPUB30991_00-NPUB309910000000.pkg?dl=1','https://www.dropbox.com/s/3dbnzijzdycyrgt/3DGAME-NPUB30991_00-NPUB309910000000.pkg?dl=1','https://www.dropbox.com/s/pzdigt75h6gnycn/2PATCH-BLUS30991_00-BLUS309910000000.pkg?dl=1','https://www.dropbox.com/s/wue66tsk5dqfvh2/Assassins%20Creed%20III%20%28Audio%20PT-BR%29.pkg?dl=1','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('7','Assassin Creed 4 Black Flag ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB31193_00-NPUB311930000000','assassins4.jpg','2020-09-02 16:28:16',
    'https://www.dropbox.com/s/4axlwn17wpa2v7i/1DGAME-NPUB31193_00-NPUB311930000000.pkg?dl=1','https://www.dropbox.com/s/e1g24d4i1do4flv/2DGAME-NPUB31193_00-NPUB311930000000.pkg?dl=1','https://www.dropbox.com/s/jv5gpq8n30wp1ls/3DGAME-NPUB31193_00-NPUB311930000000.pkg?dl=1','https://www.dropbox.com/s/cm4s8708qw9zm6o/2PATCH-BLUS31193_00-BLUS311930000000.pkg?dl=1','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('8','Assassin Creed Revelations','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPEB01467_00-NPEB014670000000','assassinsrvl.jpg','2020-09-02 16:28:20',
    'https://www.dropbox.com/s/ysypabnhos8wot2/1DGAME-NPEB01467_00-NPEB014670000000.pkg?dl=1','https://www.dropbox.com/s/f0a4yioganl16jw/2DGAME-NPEB01467_00-NPEB014670000000.pkg?dl=1','https://www.dropbox.com/s/mbqbbonf7ny4y32/3DGAME-NPEB01467_00-NPEB014670000000.pkg?dl=1','https://www.dropbox.com/s/4ed1ljwmizojx7z/2PATCH-BLES01467_00-BLES014670000000.pkg?dl=1','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('9','Assassin Creed Rogue ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB31465_00-NPUB314650000000','assassinsrogue.jpg','2020-09-02 16:28:25',
    'https://www.dropbox.com/s/e09zuqc9lu16g8y/1DGAME-NPUB31465_00-NPUB314650000000.pkg?dl=1','https://www.dropbox.com/s/du8z1z0jd3wwrnr/2DGAME-NPUB31465_00-NPUB314650000000.pkg?dl=1','https://www.dropbox.com/s/ehh5vu91rj0yyi7/2PATCH-BLUS31465_00-BLUS314650000000.pkg?dl=1','https://www.dropbox.com/s/3lpqxypynf04730/BLUS31465_ASSASSINS_CREED_ROGUE_DELUXE_DLCPACK_FIX.pkg?dl=1','https://www.dropbox.com/s/fwgsrlo77rnpuvq/BLUS31465_ASSASSINS_CREED_ROGUE_TIMESAVER_PACK_DLC_FIX.pkg?dl=1','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('10','Assassins Creed Brotherhood','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB30537_00-NPUB305370000000','assassinshood.jpg','2020-09-02 16:28:30',
    'https://www.dropbox.com/s/scxy4munly06znd/1DGAME-NPUB30537_00-NPUB305370000000.pkg?dl=1','https://www.dropbox.com/s/wz1783fn5kcje3s/2DGAME-NPUB30537_00-NPUB305370000000.pkg?dl=1','https://www.dropbox.com/s/fqculo1qyokg5k4/2PATCH-BLUS30537_00-BLUS305370000000.pkg?dl=1','https://www.dropbox.com/s/4ngy0vzl1np6463/WBIiDORaSrQeuxWDeldSyJvBFAkZKBwoPAJkCJynFPPubTcYVGQXrMxxNbCJzbNDECBFcxgVaLcbJMURcjMYinTVZhXqsoqSlexjY.pkg?dl=1','https://www.dropbox.com/s/7a13bb5ibtkbjpg/nVnppUGEXQjJfaGqbYjDvaYBxXiFMrdXIvxvItpvfrZBQcJYhiATyLwdKzMGrabaziobVPRjDRsZGcVVeKtTorSncAHfKuOvRsUIw.pkg?dl=1','https://www.dropbox.com/s/kv0v2dsdx2f4htj/Maf9oxdHw4xtMtUyOdilNeKB8E7H5anBp0wCvcog39uSa1bliXqF3oIl8Jt1ha2ILOTiTSEO13xuO2gUaqTcMhWNPVn7umIO4Owpj.pkg?dl=1','https://www.dropbox.com/s/kg8b5hkealf14vn/atrsNwMUGoscTprlBuUCfumonymAlohdqzbOTSmNqjYCkUNZQlRJfLkPEirVUUDIYpTcNEIRIALAKiMesFlOyzmfpdHMpqdVAwMvK.pkg?dl=1','https://www.dropbox.com/s/bnlpct9kc035q5f/BLUS30537_ASSASSINS_CREED_BROTHERHOOD_DA_VINCI_DLC_FIX.pkg?dl=1','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('11','Asura Wrath','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB30721_00-NPUB307210000000','asuras.jpg','2020-09-02 16:28:34',
    'https://www.dropbox.com/s/n51j7fhy19ev1mt/1DGAME-NPUB30721_00-NPUB307210000000.pkg?dl=1','https://www.dropbox.com/s/d4i4acvh728ad7s/2DGAME-NPUB30721_00-NPUB307210000000.pkg?dl=1','https://www.dropbox.com/s/kexwzy34msimnw9/2PATCH-BLUS30721_00-BLUS307210000000.pkg?dl=1','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('12','Batman Arkham Origins ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB31207_00-NPUB312070000000','batmanorigins.jpg','2020-09-02 16:28:38',
    'https://www.dropbox.com/s/w38sbgq0ak9wygl/1DGAME-NPUB31207_00-NPUB312070000000.pkg?dl=1','https://www.dropbox.com/s/ftu8vu9e60duqui/2DGAME-NPUB31207_00-NPUB312070000000.pkg?dl=1','https://www.dropbox.com/s/dqcxmh9o2cr7j9z/3DGAME-NPUB31207_00-NPUB312070000000.pkg?dl=1','https://www.dropbox.com/s/dqcxmh9o2cr7j9z/3DGAME-NPUB31207_00-NPUB312070000000.pkg?dl=1','https://www.dropbox.com/s/bm0rl5svc7tki5e/4DGAME-NPUB31207_00-NPUB312070000000.pkg?dl=1','https://www.dropbox.com/s/krzmipo2yj5aglj/2PATCH-BLUS31207_00-BLUS312070000000.pkg?dl=1','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('13','Batman Arkham City ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPEB00926_00-NPEB009260000000','batmancity.jpg','2020-09-02 16:28:42',
    'https://www.dropbox.com/s/g3ti6i2r6rnm7dv/1DGAME-NPEB00926_00-NPEB009260000000.pkg?dl=1','https://www.dropbox.com/s/jt1ipe5omystr95/2DGAME-NPEB00926_00-NPEB009260000000.pkg?dl=1','https://www.dropbox.com/s/kezl5o08okvvxsl/2PATCH-BLES00926_00-BLES009260000000.pkg?dl=1','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('14','Battle Vs Chess','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPEB00941_00-NPEB009410000000','chess.jpg','2020-09-02 16:28:46',
    'https://www.dropbox.com/s/6ci4qnt41wun2x0/1DGAME-NPEB00941_00-NPEB009410000000.pkg?dl=1','https://www.dropbox.com/s/ca6z7ax94mx5ab6/2PATCH-BLES00941_00-BLES009410000000.pkg?dl=1','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('15','Battlefield 3','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB30762_00-NPUB307620000000','bf3.jpg','2020-09-02 16:28:50',
    'https://www.dropbox.com/s/ac7kispwnyc2b99/1DGAME-NPUB30762_00-NPUB307620000000.pkg?dl=1','https://www.dropbox.com/s/nxaes6yvmez4smb/2DGAME-NPUB30762_00-NPUB307620000000.pkg?dl=1','https://www.dropbox.com/s/qkc8xzynmtiupar/3DGAME-NPUB30762_00-NPUB307620000000.pkg?dl=1','https://www.dropbox.com/s/njcb3chjj67o1e8/2PATCH-BLUS30762_00-BLUS307620000000.pkg?dl=1','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('16','Battlefield 4 ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPEB01832_00-NPEB018320000000','bf4.jpg','2020-09-02 16:28:54',
    'https://www.dropbox.com/s/0imae3jfffre4zp/1DGAME-NPEB01832_00-NPEB018320000000.pkg?dl=1','https://www.dropbox.com/s/1qheq5b3bcei1nh/2DGAME-NPEB01832_00-NPEB018320000000.pkg?dl=1','https://www.dropbox.com/s/5t5rii6yc607d51/3DGAME-NPEB01832_00-NPEB018320000000.pkg?dl=1','https://www.dropbox.com/s/u3d3mggr7ene2q2/2PATCH-BLES01832_00-BLES018320000000.pkg?dl=1','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('17','Battlefield Hardline ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1DGAME-NPUB31440_00-NPUB314400000000','bfhardline.jpg','2020-09-02 16:29:21',
    'https://www.dropbox.com/s/rk5vrir9wcaddvf/1DGAME-NPUB31440_00-NPUB314400000000.pkg?dl=1','https://www.dropbox.com/s/om846n23uomq0ib/2DGAME-NPUB31440_00-NPUB314400000000.pkg?dl=1','https://www.dropbox.com/s/xrm0ear202izpd1/3DGAME-NPUB31440_00-NPUB314400000000.pkg?dl=1','https://www.dropbox.com/s/jh2honee7zm0v18/4DGAME-NPUB31440_00-NPUB314400000000.pkg?dl=1','https://www.dropbox.com/s/i9h4dm5hp7oxue4/2PATCH-BLUS31440_00-BLUS314400000000.pkg?dl=1','---','---','---','---','---','---','---','---',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('18','Beyond Two Souls ','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','1HGAME-NPUA72074_00-NPUA720740000000','bts.jpg','2020-09-02 16:29:31',
    'https://www.dropbox.com/s/wejl62xvy91v53d/1HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/8mysrpj1vbvbfzs/2HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/z2u9qlolb1qcc4c/3HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/sjwqzgyatygwd7a/4HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/1st3drd0fdw6x7s/5HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/di94ptcw4m0prwl/6HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/clemjlgmk25qay9/7HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/jzdkip2a5v6i8kr/8HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/wmiesqxyfubfrrs/9HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/ni1hzmsd3p9cjz6/10HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/heowb2ch18l12i3/11HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/xu1s9xz4onnu1eg/12HGAME-NPUA72074_00-NPUA720740000000.pkg?dl=1','https://www.dropbox.com/s/xpaz0hqwgv0gv6m/2PATCH-BCUS99134_00-BCUS991340000000.pkg?dl=1',
    '---','---','---','---','---','---','---','---','---','---','---','---',
    '---','---','---','---','---'),
('19','a','g','g','g','2020-09-02 21:07:11',
    'g','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido','nao_inserido',
    'nao_inserido','nao_inserido','','','','','','','','','','',
    '','','','','');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_emuladores`
--

CREATE TABLE `playstation_emuladores` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_emuladores`
--

INSERT INTO `playstation_emuladores` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES
('3','Retroarch','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP0000-SLUS20223_00-PS2CLASSICS00000','retroarch.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/sqi9t251n8j8pxa/UP0000-SLUS20223_00-PS2CLASSICS00000.pkg?dl=1'),
('4','Mega Drive PGEN','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP0000-SLUS00000_00-PS2CLASSICS00000','pgen.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/d4zlz6ey1xcm989/UP0000-SLUS00000_00-PS2CLASSICS00000.pkg?dl=1'),
('5','Super Nintendo SnesStation','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP0000-SLUS00001_00-PS2CLASSICS00000','snes.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/q4miivo3x1ri61h/UP0000-SLUS00001_00-PS2CLASSICS00000.pkg?dl=1'),
('6','Nintendo System NES','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP9000-SLUS00886_00-0000000000000001','nes.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/kjlgbgfvhf7yc3f/UP9000-SLUS00886_00-0000000000000001.pkg?dl=1'),
('7','Master System','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','EP0000-SLES66654_00-PS2CLASSICS00000','mastersystem.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/vy2uv77opfpkd9v/EP0000-SLES66654_00-PS2CLASSICS00000.pkg?dl=1'),
('8','Game Boy Advanced','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP0000-SLUS20223_00-PS2CLASSICS00000','gba.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/sqi9t251n8j8pxa/UP0000-SLUS20223_00-PS2CLASSICS00000.pkg?dl=1'),
('9','Atari V1','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP9000-SLUS00777_00-0000000000000001','atari.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/fspf83xq224jf5j/UP9000-SLUS00777_00-0000000000000001.pkg?dl=1'),
('10','Atari V2','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP0000-SLUS20273_00-PS2CLASSICS00000','atari.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/p8ggd3q8kej31hq/UP0000-SLUS20273_00-PS2CLASSICS00000.pkg?dl=1'),
('11','Atari V3','Idioma: Ingles<br/> Legenda: Ingles<br/> Plataforma: PlayStation PS3','UP0000-SLUS21076_00-PS2CLASSICS00000','atari.jpg','2020-09-02 17:01:01','https://www.dropbox.com/s/rqyfa2o21v5kl7d/UP0000-SLUS21076_00-PS2CLASSICS00000.pkg?dl=1');-- --------------------------------------------------------

--
-- Estrutura da tabela `playstation_extras`
--

CREATE TABLE `playstation_extras` (
  `id` int(255) UNSIGNED NOT NULL,
  `titulo` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `descricao` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `content_id` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `imagem` mediumtext COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` mediumtext COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `playstation_extras`
--

INSERT INTO `playstation_extras` (`id`, `titulo`, `descricao`, `content_id`, `imagem`, `cadastro`, `link`) VALUES
('3','AAAAAAAAAAAA','AAAAAAAAAAAAA','AAAAAAAAAA','1AAa.jpg','2020-09-10 19:41:53','AAAAAAAAA'),
('4','AAAAAAAAAAAA','AAAAAAAAAAAAA','AAAAAAAAAA','1AAa.jpg','2020-09-10 19:41:57','AAAAAAAAA');--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `playstation_emuladores`
--
ALTER TABLE `playstation_emuladores`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_extras`
--
ALTER TABLE `playstation_extras`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_infos`
--
ALTER TABLE `playstation_infos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_ps1`
--
ALTER TABLE `playstation_ps1`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_ps2`
--
ALTER TABLE `playstation_ps2`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_ps3`
--
ALTER TABLE `playstation_ps3`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_psp`
--
ALTER TABLE `playstation_psp`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `playstation_users`
--
ALTER TABLE `playstation_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `playstation_emuladores`
--
ALTER TABLE `playstation_emuladores`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_extras`
--
ALTER TABLE `playstation_extras`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_infos`
--
ALTER TABLE `playstation_infos`
  MODIFY `id` mediumint(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_ps1`
--
ALTER TABLE `playstation_ps1`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_ps2`
--
ALTER TABLE `playstation_ps2`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_ps3`
--
ALTER TABLE `playstation_ps3`
  MODIFY `id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_psp`
--
ALTER TABLE `playstation_psp`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT de tabela `playstation_users`
--
ALTER TABLE `playstation_users`
  MODIFY `id` mediumint(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
