-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Jan 2024 pada 16.20
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `siakad`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `nrp` int(11) NOT NULL,
  `mhs_name` varchar(80) DEFAULT NULL,
  `mhs_dprt` varchar(80) DEFAULT NULL,
  `mhs_brth` varchar(80) DEFAULT NULL,
  `mhs_ipk` varchar(30) DEFAULT NULL,
  `mhs_ips` varchar(30) DEFAULT NULL,
  `mhs_lectg` varchar(80) DEFAULT NULL,
  `mhs_entr` varchar(30) DEFAULT NULL,
  `mhs_crse` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `mahasiswa`
--

INSERT INTO `mahasiswa` (`nrp`, `mhs_name`, `mhs_dprt`, `mhs_brth`, `mhs_ipk`, `mhs_ips`, `mhs_lectg`, `mhs_entr`, `mhs_crse`) VALUES
(101, 'Keeley Beltran', 'Sistem Informasi', 'Pacitan, 11 Januari 2003', ' 3.46', '3.37', 'Phoenix Floras', '2021', 'Rintisan Bisnis Digital, Manajemen Investasi TI, Proteksi Aset Informasi, Desain Pengalaman Pengguna\r\n'),
(102, 'Cian Baird', 'Sistem Informasi', 'Nganjuk, 20 Juni 2002', '3.54', '3.60', 'Ernest Barte', '2020', 'Manajemen Rantai Pasok, Teknik Peramalan, Manajemen Keberlangsungan Bisnis'),
(113, 'Eloise Navarro', 'Teknik Fisika', 'Bandung, 19 April 2001', '3.47', '3.56', 'Willie Peairs', '2019', 'Proyek Rekayasa Interdisiplin, Kewirausahaan Berbasis Teknologi, Rekayasa Konversi dan Konservasi Energi, Rekayasa Kenyamanan Termal'),
(114, 'Miya Mullen', 'Teknik Fisika', 'Semarang, 30 Agustus 2003', '3.32', '3.39', 'Johnnie Langhans', '2021', 'Fisika Bahan, Sistem Pengukuran dan Kalibrasi, Aplikasi Pengukuran, Perpindahan Panas dan Massa'),
(125, 'Martha Mclean', 'Teknologi Informasi', 'Jakarta, 4 September 2004', '3.41', '3.69', 'Kiley Buggie', '2022', 'Kriptografi, Pemrograman Integratif, Sistem Operasi, Teknologi Multimedia'),
(126, 'Zackary Roberson', 'Teknologi Informasi', 'Tangerang, 19 November 2002', '3.70', '3.71', 'Rafael Stroffolino', '2020', 'Keamanan Jaringan Nirkabel, Keamanan Web dan Aplikasi, Kecerdasan Artifisial, Komputasi Awan'),
(137, 'Matthew Lee', 'Arsitektur', 'Surabaya, 14 Mei 2002', '3.57', '3.37', 'Benjamin Cahoon', '2020', 'Perancangan Arsitektur, Asas Perancangan Arsitektur, Sejarah Arsitektur');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`nrp`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
