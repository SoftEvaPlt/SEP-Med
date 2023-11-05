/*
 Navicat Premium Data Transfer

 Source Server         : SoftEvaPlt
 Source Server Type    : MySQL
 Source Server Version : 100508 (10.5.8-MariaDB-1:10.5.8+maria~focal)
 Source Host           : localhost:3306
 Source Schema         : SoftEvaPlt

 Target Server Type    : MySQL
 Target Server Version : 100508 (10.5.8-MariaDB-1:10.5.8+maria~focal)
 File Encoding         : 65001

 Date: 05/11/2023 23:17:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for safety_indicator
-- ----------------------------
DROP TABLE IF EXISTS `safety_indicator`;
CREATE TABLE `safety_indicator`  (
  `si_id` int NOT NULL COMMENT '安全指标ID',
  `si_category` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '指标分类',
  `si_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '安全指标名称',
  `si_state` int NOT NULL DEFAULT 0 COMMENT '安全指标状态',
  `si_creator` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '安全指标创建人',
  `si_create_time` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE CURRENT_TIMESTAMP COMMENT '安全指标创建时间',
  PRIMARY KEY (`si_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of safety_indicator
-- ----------------------------

-- ----------------------------
-- Table structure for scene
-- ----------------------------
DROP TABLE IF EXISTS `scene`;
CREATE TABLE `scene`  (
  `scene_id` int NOT NULL COMMENT '场景ID',
  `scene_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '场景名称',
  `scene_state` int NOT NULL DEFAULT 0 COMMENT '场景状态',
  `scene_description` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '场景描述',
  `scene_creator` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '场景创建人',
  `scene_create_time` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE CURRENT_TIMESTAMP COMMENT '场景创建时间',
  PRIMARY KEY (`scene_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of scene
-- ----------------------------

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task`  (
  `task_id` int NOT NULL COMMENT '任务ID',
  `task_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '任务名称',
  `task_state` int NOT NULL DEFAULT 0 COMMENT '任务状态',
  `scene_id` int NOT NULL COMMENT '应用场景（场景ID）',
  `task_creator` int NOT NULL COMMENT '任务创建人（用户ID）',
  `task_create_time` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE CURRENT_TIMESTAMP COMMENT '任务创建时间',
  `product_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '产品名称',
  `product_version` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '产品版本号',
  `product_description` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '产品描述',
  `product_TD` blob NULL COMMENT '产品拓扑图',
  `product_AD` blob NULL COMMENT '产品架构图',
  `app_IP` int UNSIGNED NULL DEFAULT NULL COMMENT '应用IP',
  `app_domain_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '应用域名',
  `app_starting_URL` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '起始URL',
  `app_port` int NULL DEFAULT NULL COMMENT '应用端口',
  `app_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '应用名称',
  `app_os_version` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '操作系统版本',
  PRIMARY KEY (`task_id`) USING BTREE,
  UNIQUE INDEX `task_name`(`task_name` ASC) USING BTREE,
  UNIQUE INDEX `product_name`(`product_name` ASC) USING BTREE,
  INDEX `scene_id`(`scene_id` ASC) USING BTREE,
  INDEX `task_creator`(`task_creator` ASC) USING BTREE,
  CONSTRAINT `task_ibfk_1` FOREIGN KEY (`scene_id`) REFERENCES `scene` (`scene_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_ibfk_2` FOREIGN KEY (`task_creator`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task
-- ----------------------------

-- ----------------------------
-- Table structure for task_evaluation
-- ----------------------------
DROP TABLE IF EXISTS `task_evaluation`;
CREATE TABLE `task_evaluation`  (
  `user_id` int NOT NULL COMMENT '用户ID',
  `task_id` int NOT NULL COMMENT '任务ID',
  `task_evaluate_time` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE CURRENT_TIMESTAMP COMMENT '评审时间',
  PRIMARY KEY (`user_id`, `task_id`) USING BTREE,
  INDEX `task_id`(`task_id` ASC) USING BTREE,
  CONSTRAINT `task_evaluation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_evaluation_ibfk_2` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task_evaluation
-- ----------------------------

-- ----------------------------
-- Table structure for task_operation
-- ----------------------------
DROP TABLE IF EXISTS `task_operation`;
CREATE TABLE `task_operation`  (
  `user_id` int NOT NULL COMMENT '用户ID',
  `task_id` int NOT NULL COMMENT '任务ID',
  `task_operate_time` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE CURRENT_TIMESTAMP COMMENT '最后操作时间',
  PRIMARY KEY (`user_id`, `task_id`) USING BTREE,
  INDEX `task_id`(`task_id` ASC) USING BTREE,
  CONSTRAINT `task_operation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_operation_ibfk_2` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task_operation
-- ----------------------------

-- ----------------------------
-- Table structure for task_si
-- ----------------------------
DROP TABLE IF EXISTS `task_si`;
CREATE TABLE `task_si`  (
  `task_id` int NOT NULL COMMENT '任务ID',
  `si_id` int NOT NULL COMMENT '安全指标ID',
  PRIMARY KEY (`task_id`, `si_id`) USING BTREE,
  INDEX `si_id`(`si_id` ASC) USING BTREE,
  CONSTRAINT `task_si_ibfk_1` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `task_si_ibfk_2` FOREIGN KEY (`si_id`) REFERENCES `safety_indicator` (`si_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task_si
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `user_id` int NOT NULL COMMENT '用户ID',
  `user_account` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户账号',
  `user_password` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户密码',
  `user_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户账号',
  `user_authority` int NOT NULL DEFAULT 0 COMMENT '用户权限',
  `user_email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '用户邮箱',
  `user_phone` int NULL DEFAULT NULL COMMENT '用户电话号码',
  PRIMARY KEY (`user_id`) USING BTREE,
  UNIQUE INDEX `user_account`(`user_account` ASC) USING BTREE,
  UNIQUE INDEX `user_name`(`user_name` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
