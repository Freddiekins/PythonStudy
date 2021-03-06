/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : testdb

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 25/06/2020 04:53:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '',
  `age` tinyint UNSIGNED NULL DEFAULT 0,
  `height` decimal(5, 2) NULL DEFAULT NULL,
  `gender` enum('男','女','中性','保密') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '保密',
  `cls_id` int UNSIGNED NULL DEFAULT 0,
  `is_delete` bit(1) NULL DEFAULT b'0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES (15, '小明', 18, 180.00, '女', 1, b'0');
INSERT INTO `students` VALUES (16, '小月月', 18, 180.00, '女', 2, b'1');
INSERT INTO `students` VALUES (17, '彭于晏', 29, 185.00, '男', 1, b'0');
INSERT INTO `students` VALUES (18, '刘德华', 59, 175.00, '男', 2, b'1');
INSERT INTO `students` VALUES (19, '黄蓉', 38, 160.00, '女', 1, b'0');
INSERT INTO `students` VALUES (20, '凤姐', 28, 150.00, '保密', 2, b'1');
INSERT INTO `students` VALUES (21, '王祖贤', 18, 172.00, '女', 1, b'1');
INSERT INTO `students` VALUES (22, '周杰伦', 36, NULL, '男', 1, b'0');
INSERT INTO `students` VALUES (23, '程坤', 27, 181.00, '男', 2, b'0');
INSERT INTO `students` VALUES (24, '刘亦菲', 25, 166.00, '女', 2, b'0');
INSERT INTO `students` VALUES (25, '金星', 33, 162.00, '中性', 3, b'1');
INSERT INTO `students` VALUES (26, '静香', 12, 180.00, '女', 4, b'0');
INSERT INTO `students` VALUES (27, '郭靖', 12, 170.00, '男', 4, b'0');
INSERT INTO `students` VALUES (28, '周杰', 34, 176.00, '女', 5, b'0');

SET FOREIGN_KEY_CHECKS = 1;
