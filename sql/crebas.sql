/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     29/8/2016 1:56:34 a. m.                      */
/*==============================================================*/
CREATE DATABASE test;

USE test;

drop table if exists DEPARTAMENTOS;

drop table if exists LOCALIDADES;

/*==============================================================*/
/* Table: DEPARTAMENTOS                                         */
/*==============================================================*/
create table DEPARTAMENTOS
(
   ID_DEPARTAMENTO      int not null auto_increment,
   NOMBRE_DEPARTAMENTO  varchar(100),
   primary key (ID_DEPARTAMENTO)
);

/*==============================================================*/
/* Table: LOCALIDADES                                           */
/*==============================================================*/
create table LOCALIDADES
(
   ID_LOCALIDAD         int not null auto_increment,
   ID_DEPARTAMENTO      int not null,
   NOMBRE_LOCALIDAD     varchar(100),
   primary key (ID_LOCALIDAD)
);

alter table LOCALIDADES add constraint FK_LOCALIDAD_DEPARTAMENTO foreign key (ID_DEPARTAMENTO)
      references DEPARTAMENTOS (ID_DEPARTAMENTO) on delete restrict on update restrict;

