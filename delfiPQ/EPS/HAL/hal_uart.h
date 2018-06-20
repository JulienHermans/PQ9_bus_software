#ifndef __HAL_UART_H
#define __HAL_UART_H

#include <stdint.h>
#include <satellite.h>

//extern UART_Handle uart_dbg_bus;

SAT_returnState HAL_uart_rx(dev_id id, uint8_t *buf, uint16_t *size);

void HAL_uart_tx(dev_id id, uint8_t *buf, uint16_t size);

void HAL_PQ9_BUS_enable_tx();

SAT_returnState HAL_SPI_readWrite(dev_id id,
                                  void *writeBuf,
                                  size_t count,
                                  void *readBuf);

SAT_returnState HAL_I2C_readWrite(dev_id id,
                                  void *writeBuf,
                                  size_t tx_count,
                                  void *readBuf,
                                  size_t rx_count);

void HAL_eps_v1_OFF();
void HAL_eps_v1_ON();

void HAL_eps_v2_OFF();
void HAL_eps_v2_ON();

void HAL_eps_v3_OFF();
void HAL_eps_v3_ON();

void HAL_eps_v4_OFF();
void HAL_eps_v4_ON();

#endif