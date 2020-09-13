--     ████████╗ ██████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
--     ╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
--        ██║   ██║      ╚███╔╝ ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
--        ██║   ██║      ██╔██╗ ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
--        ██║   ╚██████╗██╔╝ ██╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
--        ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
-- @Gorpo Orko - 2020 

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

-- --------------------------------------------------------
--
-- Estrutura da tabela `usuario`
--

CREATE TABLE `playstation_users` (
  `id` MEDIUMINT NOT NULL AUTO_INCREMENT,
  `usuario` varchar(200) NOT NULL,
  `senha` varchar(329) NOT NULL,
  `nome` varchar(999) NOT NULL,
  `cadastro` datetime NOT NULL,
  `nivel` varchar(999) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `usuario`
--

INSERT INTO `playstation_users` (`id`, `usuario`, `senha`, `nome`, `cadastro`,`nivel`) VALUES
(0, 'marcinho', 'marcinho', 'Marcinho', '2500-01-11 19:42:12','user'),
(1, 'gorpo', 'gorpo', 'Gorpo', '2500-01-11 19:42:12','admin'),
(2, 'gorp', 'corp', 'Gorpo', '2500-01-11 19:42:12','admin'),
(3, 'gorpo', 'corpo', 'Gorpo', '2500-01-11 19:42:12','admin'),
(4,'mitsuki', 'tcxsproject2020web', 'Mitsuki', '2500-09-07 15:06:19','admin'),
(5,'mste3dz', 'tcxsproject2020web', 'MsTe3dz', '2500-09-07 15:06:25','admin'),
(6,'mit', 'mit', 'Mitsuki', '2500-09-07 15:06:25','admin'),
(7,'ted', 'ted', 'MsTe3dz', '2500-09-07 15:06:25','admin');


--
-- Estrutura da tabela `home informacoes`
--

CREATE TABLE `playstation_infos` (
  `id` MEDIUMINT NOT NULL AUTO_INCREMENT,
  `informacao` varchar(999) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Estrutura da tabela `jogos psp`
--

CREATE TABLE `playstation_psp` (
  `id` int(255) PRIMARY KEY AUTO_INCREMENT,
  `titulo` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `content_id` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `imagem` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` varchar(999999) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Estrutura da tabela `jogos ps1`
--

CREATE TABLE `playstation_ps1` (
  `id` int(255) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `titulo` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `content_id` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `imagem` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` varchar(999999) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


--
-- Estrutura da tabela `jogos ps2`
--

CREATE TABLE `playstation_ps2` (
  `id` int(255) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `titulo` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `content_id` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `imagem` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` varchar(999999) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Estrutura da tabela `jogos ps3`
--

CREATE TABLE `playstation_ps3` (
  `id` int(255) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `titulo` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `content_id` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `imagem` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link1` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link2` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link3` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link4` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link5` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link6` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link7` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link8` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link9` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link10` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link11` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link12` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link13` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link14` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link15` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link16` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link17` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link18` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link19` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link20` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link21` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link22` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link23` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link24` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link25` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link26` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link27` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link28` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link29` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `link30` varchar(999999) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Estrutura da tabela `jogos ps_emuladores`
--

CREATE TABLE `playstation_emuladores` (
  `id` int(255) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `titulo` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `content_id` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `imagem` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` varchar(999999) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;




--
-- Estrutura da tabela `jogos extras`
--

CREATE TABLE `playstation_extras` (
  `id` int(255) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `titulo` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `descricao` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `content_id` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `imagem` varchar(999999) COLLATE utf8_unicode_ci NOT NULL,
  `cadastro` datetime NOT NULL,
  `link` varchar(999999) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


