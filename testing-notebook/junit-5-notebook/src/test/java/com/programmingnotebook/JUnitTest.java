package com.programmingnotebook;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class JUnitTest {

    @Test
    void minimumRequirementForWritingATestCase() {
        Assertions.assertEquals(20, 10 + 10);
    }
}
