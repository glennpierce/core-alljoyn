/*
 * Buffer.cc
 *
 *  Created on: Jun 1, 2015
 *      Author: erongo
 */
/******************************************************************************
 * Copyright AllSeen Alliance. All rights reserved.
 *
 *    Permission to use, copy, modify, and/or distribute this software for any
 *    purpose with or without fee is hereby granted, provided that the above
 *    copyright notice and this permission notice appear in all copies.
 *
 *    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 *    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 *    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 *    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 *    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 *    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 *    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 ******************************************************************************/
#include "Buffer.h"

namespace nio {

Buffer::Buffer()
{
    m_buffer = nullptr;
    m_capacity = 0;
    m_length = 0;
}

Buffer::Buffer(uint8_t* buf, uint32_t buflen, uint32_t capacity)
{
    Set(buf, buflen, capacity);
}

Buffer::~Buffer()
{
    printf("~Buffer(%p)\n", this);
    //delete [] m_buffer;
}

void Buffer::Set(uint8_t* buf, uint32_t buflen, uint32_t capacity)
{
    m_buffer = buf;
    m_length = buflen;
    m_capacity = capacity;
}

uint8_t* Buffer::GetBuffer()
{
    return m_buffer;
}

uint32_t Buffer::GetLength()
{
    return m_length;
}

uint32_t Buffer::GetCapacity()
{
    return m_capacity;
}

} /* namespace nio */