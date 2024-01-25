-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 25-01-2024 a las 11:08:29
-- Versión del servidor: 8.2.0
-- Versión de PHP: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ahorcado`
--
CREATE DATABASE IF NOT EXISTS `ahorcado` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `ahorcado`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `intentos_usuarios`
--

DROP TABLE IF EXISTS `intentos_usuarios`;
CREATE TABLE IF NOT EXISTS `intentos_usuarios` (
  `id_intento` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `intentos` int DEFAULT NULL,
  `intentos_fallados` int NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_intento`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `intentos_usuarios`
--

INSERT INTO `intentos_usuarios` (`id_intento`, `id_usuario`, `intentos`, `intentos_fallados`, `fecha`) VALUES
(7, 3, 9, 1, '2024-01-25 10:20:30'),
(8, 6, 8, 3, '2024-01-25 10:29:36'),
(9, 7, 8, 3, '2024-01-25 10:30:59'),
(10, 8, 9, 4, '2024-01-25 10:33:05');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `unique` (`nombre`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`) VALUES
(3, 'Adrian'),
(4, 'Alberto'),
(6, 'Andres'),
(7, 'Calvo'),
(8, 'foca');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
